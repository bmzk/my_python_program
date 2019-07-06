# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\asd\\Documents\\GitHub\\my_python_program\\GetTime\\GetTime.py'],
             pathex=['C:\\Users\\asd\\Documents\\GitHub\\my_python_program\\GetTime'],
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
          name='GetTime',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
