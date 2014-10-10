# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kinfocenter

# >> macros
# << macros

Summary:    KDE Info Center
Version:    5.1.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kinfocenter.yaml
Source101:  kinfocenter-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kcmutils-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kio-devel
BuildRequires:  plasma-devel
BuildRequires:  kservice-devel
BuildRequires:  solid-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libGL-devel
BuildRequires:  libEGL-devel

%description
KDE Info Center


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING COPYING.DOC
%{_kf5_bindir}/kinfocenter
%{_kf5_plugindir}/*
%{_kf5_sharedir}/*
%{_kf5_configdir}/menus/kinfocenter.menu
%{_kf5_sharedir}/desktop-directories/kinfocenter.directory
%{_kf5_sharedir}/applications/*.desktop
%{_kf5_htmldir}/en/kinfocenter
%{_kf5_servicesdir}/*
%{_kf5_servicetypesdir}/*
# >> files
# << files
