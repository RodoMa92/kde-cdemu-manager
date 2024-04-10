Name:           kde-cdemu-manager
Version:        0.8.2
Release:        0
Summary:        Frontend to CDEmu
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/marcelh83/kde-cdemu-manager
Source0:        https://github.com/RodoMa92/kde-cdemu-manager/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  breeze-icon-theme
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
Requires:       cdemu-daemon
Recommends:     %{name}-lang

%description
KDE CDEmu Manager is a simple frontend for CDEmu.

It provides a small manager window that gives you an overview of your
virtual drives and allows you to mount and unmount images.

It also includes a service menu for mounting images directly from
Dolphin/Konqueror.

%lang_package

%prep
%setup -q

%build
%{cmake} -DBUILD_SHARED_LIBS:BOOL=OFF
cd redhat-linux-build
make %{?_smp_mflags}

%install
cd redhat-linux-build
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_kf5_bindir}/kde_cdemu
%{_kf5_datadir}/applications/org.kde.kde_cdemu.desktop
%{_kf5_datadir}/kservices5/ServiceMenus/kde_cdemu_mount.desktop
%{_kf5_datadir}/locale

%changelog
%autochangelog
