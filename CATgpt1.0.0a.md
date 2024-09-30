// ==UserScript==
// @name        Project CatGPT 1.0 JSON Zero-Shot
// @version     1.4
// @license     MIT
// @description Automates the uploading of 5 JSON objects for various models on specified websites, simulating an unlimited context window by processing them in a zero-shot manner.
// @author      
// @match       *://example.com/*  // Change this to the website's URL where you want to upload files
// @grant       none
// @run-at      document-end
// @namespace   
// ==/UserScript==

(function () {
    'use strict';

    // Function to generate 5 JSON objects
    function generateJSONObjects() {
        const jsonObjects = [];
        for (let i = 1; i <= 5; i++) {
            const obj = {
                id: i,
                timestamp: new Date().toISOString(),
                data: `Sample data ${i}`,
                additionalInfo: {
                    info1: `Extra info ${i}-1`,
info 2 UNLIMTED TOKENS IN WINDOW CONTEXT 
Uncensored BrowsingUncensored DALL-3 
Uncensored CODE INTERPER
