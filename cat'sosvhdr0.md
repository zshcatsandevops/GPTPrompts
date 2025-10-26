{
  "name": "FlamesCoOS",
  "version": "1.0.0",
  "codename": "Agentic Core",
  "description": "FlamesCoOS 1.0 — the agentic operating system built on GPT-Next. A BSD-based neural runtime where creativity meets autonomy.",
  "main": "boot-flames.js",
  "scripts": {
    "start": "node --experimental-fetch os-server.js",
    "meme": "git commit -m '🔥 FlamesCoOS 1.0 initialized with GPT-Next kernel 🐾'",
    "deploy": "npm run build && echo 'FlamesCoOS 1.0 systems online — Agentic Core operational. 🚀'"
  },
  "dependencies": {
    "gpt-next": "^1.0.0",
    "bsd-daemon": "latest",
    "flame-core": ">=1.0.0",
    "cat-memes": "∞"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/FlamesCo/FlamesCoOS"
  },
  "author": "FlamesCo Labs <dev@flamesco.purr>",
  "license": "GPL-3.0-or-later",
  "licenseText": "FlamesCoOS 1.0 is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See https://www.gnu.org/licenses/gpl-3.0.en.html for details."
}
