Name:           kde-cdemu-manager-kf6
Version:        0.9
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
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-knotifications-devel
BuildRequires:  kf6-kxmlgui-devel
BuildRequires:	kf6-kstatusnotifieritem-devel
BuildRequires:	kf6-kcoreaddons-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
Requires:       cdemu-daemon
Recommends:  	%{name}-lang

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
%{_kf6_bindir}/kde_cdemu
%{_kf6_datadir}/applications/org.kde.kde_cdemu.desktop
%{_kf6_datadir}/kservices5/ServiceMenus/kde_cdemu_mount.desktop
%{_kf6_datadir}/locale

%changelog
%autochangelog
