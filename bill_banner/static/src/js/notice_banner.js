/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onMounted, useState, xml } from "@odoo/owl";
import { jsonrpc } from "@web/core/network/rpc_service";

export class NoticeBanner extends Component {
    static template = xml`
        <div t-if="state.isVisible" class="oe_notice_banner alert alert-warning alert-dismissible" role="alert">
            <button type="button" class="btn-close" aria-label="Close" t-on-click="closeBanner"></button>
            <span t-att-class="{'notice-message': true, 'scroll-text': state.isReadyForScroll}" t-esc="state.messages[state.currentMessageIndex]"/>
        </div>
    `;
    
    setup() {
        this.state = useState({
            messages: [], // Changed to array
            currentMessageIndex: 0, // New state for current message index
            isActive: false,
            isVisible: false,
            isReadyForScroll: false // New state for controlling scroll class
        });
        
        onMounted(() => {
            this.loadNoticeBanner();
        });
    }
    
    startMessageCycle() {
        // Clear any existing interval to prevent multiple intervals running
        if (this.messageInterval) {
            clearInterval(this.messageInterval);
        }
        // Cycle messages every 5 seconds (adjust as needed)
        this.messageInterval = setInterval(() => {
            this.displayNextMessage();
        }, 5000);
    }

    displayNextMessage() {
        if (this.state.messages.length > 1 && this.el) {
            const messageElement = this.el.querySelector('.notice-message');
            if (messageElement) {
                messageElement.classList.add('fade-out');
                setTimeout(() => {
                    this.state.currentMessageIndex = (this.state.currentMessageIndex + 1) % this.state.messages.length;
                    messageElement.classList.remove('fade-out');
                    messageElement.classList.add('fade-in');
                    setTimeout(() => {
                        messageElement.classList.remove('fade-in');
                    }, 500); // Match fade-in animation duration
                }, 500); // Match fade-out animation duration
            }
        }
    }

    async loadNoticeBanner() {
        try {
            // Assuming the backend now returns an array of messages
            const data = await jsonrpc('/get_notice_banner', {});
            if (data && data.is_active && data.messages && data.messages.length > 0) {
                this.state.messages = data.messages; // Assign array of messages
                this.state.isActive = true;
                this.state.isVisible = true;
                this.state.currentMessageIndex = 0; // Start with the first message
                this.state.isReadyForScroll = true; // Set to true when messages are loaded
                this.startMessageCycle(); // Start cycling messages here
            } else {
                // If no active messages, hide the banner and clear interval
                this.state.isActive = false;
                this.state.isVisible = false;
                if (this.messageInterval) {
                    clearInterval(this.messageInterval);
                }
            }
        } catch (error) {
            console.error("Error loading notice banner:", error);
            // Show fallback message
            this.state.messages = ["Notice banner (connection error)"]; // Fallback as array
            this.state.isActive = true;
            this.state.isVisible = true;
            this.state.currentMessageIndex = 0;
            this.state.isReadyForScroll = true; // Set to true for fallback messages
            this.startMessageCycle(); // Start cycling for fallback message as well
        }
    }
    
    closeBanner() {
        this.state.isVisible = false;
    }
}

// Register as a main component
registry.category("main_components").add("NoticeBanner", {
    Component: NoticeBanner,
});