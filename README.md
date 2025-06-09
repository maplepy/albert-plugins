# Albert Plugins Collection

Custom plugins for the [Albert launcher](https://albertlauncher.github.io/).

![Albert](https://img.shields.io/badge/Albert-Launcher-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.7+-green?style=flat-square)

## 🚀 Overview

This directory contains Albert launcher plugins I made to enhance my experience with the launcher.

## 📦 Available Plugins

| Plugin | Status | Version | Description | Features | Installation |
|--------|--------|---------|-------------|----------|--------------|
| **🎮 ProtonDB Search** | ✅ Stable | v1.0.0 | Search Steam game compatibility ratings on ProtonDB | • Smart search algorithm<br/>• 250k+ games database<br/>• All rating tiers<br/>• Rate limiting & caching | [📖 Guide](protondb/README.md) |

## 🛠️ Quick Start

### Prerequisites

- Albert Launcher with Python plugin support
- Python 3.7+

### Installation

1. **Navigate to the plugin directory:**
   ```bash
   cd ~/.local/share/albert/python/plugins
   ```

2. **Install the ProtonDB plugin:**
   ```bash
   cd protondb
   chmod +x install.sh
   ./install.sh
   ```

3. **Enable in Albert:**
   - Open Albert settings (`Ctrl+,`)
   - Go to **Extensions** tab
   - Enable "ProtonDB Search" plugin
   - Restart Albert

## 🎯 Plugin Details

### 🎮 ProtonDB Search Plugin

Search for Steam game compatibility ratings directly from Albert.

**Usage:**
```
proton R.E.P.O
proton baldur's gate
proton for honor
```

**Key Features:**
- Fast search through 250k+ Steam games
- ProtonDB compatibility ratings
- Smart matching and caching

**[📖 Full Documentation](protondb/README.md)**

## 🔧 Development

### Contributing

1. Create a new plugin directory
2. Follow Albert's plugin API specifications
3. Include error handling and rate limiting
4. Provide installation scripts
5. Write thorough documentation with usage examples

## 🐛 Troubleshooting

**Plugin not appearing:** Check Albert has Python support enabled and restart Albert.

**Module errors:** Install missing dependencies with `pip install -r requirements.txt`

## 📄 License

MIT License - see individual plugin directories for details.
