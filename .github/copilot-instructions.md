# Ablockalypse Resource Pack - AI Coding Agent Instructions

## Project Overview
This is the **Ablockalypse Resource Pack** for Minecraft, transforming vanilla blocks and items into modern urban/industrial assets for the OmegaMinecraft apocalypse server. The pack supports Minecraft versions 1.13-1.21+ through format overlays and integrates with ModelEngine, MythicHUD, and custom server assets.

## Architecture & Multi-Version Support

### Format Overlay System
- **Base pack**: `pack_format: 13` (MC 1.20+) with `supported_formats: 13-46` in `pack.mcmeta`
- **Version overlays**: 
  - `mythichud-modern/` (formats 32-34) - Contains version-specific shaders
  - `mythichud-modern-plus/` (formats 42-46) - Latest version compatibility
- Overlays inherit and override base pack assets automatically

### Asset Organization
```
assets/
├── minecraft/          # Core Minecraft overrides
│   ├── blockstates/    # Block state definitions with random rotations
│   ├── models/         # 3D models (block/, item/, cosmetic/, custom/)
│   ├── textures/       # Urban/industrial themed textures
│   ├── sounds.json     # Custom urban animal sounds
│   └── lang/en_us.json # Complete vanilla localization override
├── modelengine/        # ModelEngine plugin integration
├── mythichud/          # MythicHUD plugin assets
└── omega/              # OmegaMinecraft server-specific assets
```

## Core Development Patterns

### Block State Random Rotations
**Critical Pattern**: Most blocks use 7-8 rotation variants to eliminate repetitive visual patterns:
```json
"variants": {
  "": [
    { "model": "block/granite" },
    { "model": "block/granite", "x": 90 },
    { "model": "block/granite", "x": 180 },
    { "model": "block/granite", "x": 270 },
    { "model": "block/granite", "y": 90 },
    { "model": "block/granite", "y": 180 },
    { "model": "block/granite", "y": 270 }
  ]
}
```
Apply this pattern to all simple blocks. Complex blocks (rails, doors) use state-specific models instead.

### Urban Industrial Theme Logic
- **Concrete blocks** → Modern building materials (glass, steel, composite panels)
- **Stone variants** → Urban surfaces (granite → bathroom tiles, andesite → concrete slabs)  
- **Ores** → Infrastructure (coal_ore → asphalt, iron_ore → manholes, copper_ore → grating)
- **Rails** → Cables/chains with 3D tie models using Blockbench JSON format
- **Nature blocks** → Decay/urban nature (lily_pad → sewer grate, kelp → trash)

### Custom Sound Integration
Urban animal sounds in `sounds.json`:
- All categorized as `"category":"hostile"` for proper audio mixing
- Files: `pigeon_1/2`, `rat_1/2`, `raven_1/2`, `seagull_1/2` in `assets/minecraft/sounds/ablockalypse/`

## Development Workflows

### Adding New Block Textures
1. **Create texture**: Place in `assets/minecraft/textures/block/` with vanilla naming
2. **Define blockstate**: Add to `assets/minecraft/blockstates/` with 7-8 rotation variants (see pattern above)
3. **Custom models**: If complex geometry needed, create in `assets/minecraft/models/block/` using Blockbench format
4. **Test in-game**: Verify rotation randomization and theme consistency

### 3D Model Creation (Rails, Complex Blocks)
- Use Blockbench for model creation with proper UV mapping
- Save as JSON format in `assets/minecraft/models/block/`
- Reference textures via `"textures": {"0": "block/texture_name"}` pattern
- Example: `activator_rail.json` has 3D tie structures with proper rotations

### Plugin Integration Points
- **ModelEngine**: Custom 3D assets in `assets/modelengine/models/` and `textures/`
- **MythicHUD**: UI elements in `assets/mythichud/textures/` and fonts
- **OmegaMinecraft**: Server-specific models in `assets/omega/`

### Multi-Version Compatibility Testing
- Base pack (`pack_format: 13`) must work on MC 1.20+
- Shader overlays in `mythichud-modern/` (1.20.2-1.20.4) and `mythichud-modern-plus/` (1.21+)
- Test format inheritance: overlays automatically inherit base assets

## Critical File Patterns

### Complete Localization Override
`assets/minecraft/lang/en_us.json` contains **6884 lines** of complete vanilla text overrides - maintain consistency when adding new items.

### Texture Organization
- Block textures: 600+ files following vanilla naming in `textures/block/`
- Animated textures: Use `.png.mcmeta` files for animation data
- Special cases: `chiseled_bookshelf/` subdirectory for state variants

### Asset Dependencies
```
blockstates/*.json → models/block/*.json → textures/block/*.png
sounds.json → sounds/ablockalypse/*.ogg
overlays/ → inherit base assets + version-specific overrides
```