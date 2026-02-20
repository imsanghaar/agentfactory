#!/usr/bin/env node
/**
 * Cross-platform build script for Docusaurus
 * Handles Node.js version-specific flags for localstorage
 */

const { execSync } = require('child_process');
const path = require('path');

// Change to learn-app directory
const learnAppDir = path.join(__dirname, '..');
process.chdir(learnAppDir);

// Get Node.js version
const nodeVersion = parseInt(process.version.slice(1).split('.')[0], 10);

// Build heap size option for OG image generation
const heapSize = '--max-old-space-size=4096';

// Build command options
let nodeOptions = heapSize;

// Node.js 25+ requires --localstorage-file flag
if (nodeVersion >= 25) {
  nodeOptions += ' --localstorage-file=/tmp/docusaurus-localstorage';
}

// Set environment variable
process.env.NODE_OPTIONS = nodeOptions;

console.log(`Building with Node.js ${process.version}...`);
console.log(`NODE_OPTIONS: ${nodeOptions}`);

try {
  // Run docusaurus build
  execSync('npx docusaurus build', {
    stdio: 'inherit',
    env: process.env
  });
  console.log('Build completed successfully!');
} catch (error) {
  console.error('Build failed:', error.message);
  process.exit(1);
}
