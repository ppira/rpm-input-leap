%global package_version 3.0.2
%global tarname v%{package_version}.tar.gz

%global rdnn_name io.github.input_leap.InputLeap

Summary: Keyboard and mouse sharing solution
Name: input-leap
Version: %{package_version}
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Daemons
URL: https://github.com/input-leap/input-leap
# Run cmake package_source to get this tarball
Source0: https://github.com/input-leap/input-leap/archive/refs/tags/v%{package_version}.tar.gz

BuildRequires: pkgconfig(avahi-compat-libdns_sd)
BuildRequires: cmake >= 3
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xtst) pkgconfig(xinerama) pkgconfig(xrandr)
BuildRequires: pkgconfig(ice) pkgconfig(sm)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Linguist)
BuildRequires: make
BuildRequires: pkgconfig(libei-1.0)
BuildRequires: pkgconfig(libportal) >= 0.8

%description
InputLeap allows you to share one mouse and keyboard between multiple computers.
Work seamlessly across Windows, macOS and Linux.

%prep
%setup -q -n %{tarname}


%build
%{cmake} . \
    -DINPUTLEAP_VERSION_DESC:STRING=%{package_version} \
    -DINPUTLEAP_BUILD_LIBEI=ON \
    -DINPUTLEAP_BUILD_TESTS=ON \
    -DINPUTLEAP_USE_EXTERNAL_GTEST=True \
    -DINPUTLEAP_VERSION_STAGE:STRING=
%{cmake_build}


%install
%{cmake_install}

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  --set-icon=%{_datadir}/icons/hicolor/scalable/apps/%{rdnn_name}.svg \
  %{buildroot}%{_datadir}/applications/%{rdnn_name}.desktop

%check
%ctest
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{rdnn_name}.desktop

%files
# None of the documentation files are actually useful here, they all point to
# the online website, so include just one, the README
%doc LICENSE ChangeLog res/Readme.txt doc/%{name}.conf.example*
%{_bindir}/%{name}c
%{_bindir}/%{name}s
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{rdnn_name}.svg
%{_datadir}/applications/%{rdnn_name}.desktop
%{_datadir}/metainfo/%{rdnn_name}.appdata.xml
%{_mandir}/man1/%{name}c.1*
%{_mandir}/man1/%{name}s.1*

%changelog
* Thu Mar 21 2019 wendall911 <wendallc@83864.com>
- Actual working spec file for Fedora

* Sat Jan 27 2018 Debauchee <todo@mail.com>
- Initial version of the package

