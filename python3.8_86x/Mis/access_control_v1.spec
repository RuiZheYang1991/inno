# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['access_control_v1.py'],
             pathex=['C:\\Users\\yang\\python3.8_86x\\venv\\Lib\\site-packages\\shiboken2', 'C:\\Users\\yang\\python3.8_86x\\Mis'],
             binaries=[],
             datas=[],
             hiddenimports=['PySide2.QtXml'],
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
          name='access_control_v1',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='icon\\ico.ico')
