pkgname = "arcan"
pkgver = "0.7.0.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DAPPL_DEST=share/arcan/appl",
    "-DDISTR_TAG=chimera",
]
cmake_dir = "src"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "chimerautils-devel",
    "ffmpeg-devel",
    "fontconfig-devel",
    "freetype-devel",
    "libdrm-devel",
    "libffi8-devel",
    "libseat-devel",
    "libusb-devel",
    "libxkbcommon-devel",
    "luajit-devel",
    "mesa-devel",
    "mesa-egl-libs",
    "mesa-gbm-devel",
    "musl-bsd-headers",
    "musl-devel",
    "openal-soft-devel",
    "pixman-devel",
    "sdl2-compat-devel",
    "sqlite-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
    "xcb-util-devel",
    "xcb-util-wm-devel",
    "xz-devel",
]
pkgdesc = "Display server, multimedia framework, and desktop engine"
license = "GPL-2.0-or-later AND BSD-3-Clause AND LGPL-2.1-only"
url = "https://arcan-fe.com"
source = f"https://github.com/letoram/arcan/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "63d925d100389e7a1074a8746a080a01d94739df487c2f8e311eb49adc006c6e"
tool_flags = {
    "CFLAGS": ["-Wno-incompatible-pointer-types"],
    "LDFLAGS": ["-lfts"],
}


@subpackage("arcan-devel")
def _(self):
    return self.default_devel()


@subpackage("arcan-encode")
def _(self):
    self.subdesc = "media encode frameserver"
    self.depends = [self.parent]
    return ["usr/bin/afsrv_encode"]


def post_install(self):
    self.install_license("COPYING")
