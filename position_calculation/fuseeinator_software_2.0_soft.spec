# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['fuseeinator_software_2.0_soft.py'],
             pathex=['C:\\Users\\Eric\\Desktop\\TEST_ARNAUD\\atom_project\\atom_python\\fuseeinator_2.0\\fuseeinator-2.0\\position_calculation'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='fuseeinator_software_2.0_soft',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='icon_software_2.ico')
