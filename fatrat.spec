%define beta beta2

Summary:	Download manager for Linux with the help of the Qt4 library
Name:		fatrat
Version:	1.2.0
Release:	0.%{beta}.1
License:	GPLv2+
Group:		Networking/File transfer
Url:		https://fatrat.dolezel.info/
Source0:	http://www.dolezel.info/download/data/fatrat/%{name}-%{version}_%{beta}.tar.xz
Patch0:		fatrat-headers.patch
Patch10:	fatrat-remove-java-applet.patch
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	gloox-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libssh2)
BuildRequires:	pkgconfig(libtorrent-rasterbar)
BuildRequires:	pkgconfig(pion-net)
BuildRequires:	pkgconfig(QtWebKit)
Requires:	qt4-common
Suggests:	fatrat-czshare
Suggests:	fatrat-opensubtitles
Suggests:	fatrat-unpack

%description
FatRat is an open source download manager for Linux/Unix systems written
in C++ with the help of the Trolltech Qt 4 library. It is rich in features
and is continuously developed.

%files -f %{name}.lang
%{_datadir}/%{name}/AUTHORS
%{_datadir}/%{name}/INSTALL
%{_datadir}/%{name}/LICENSE
%{_datadir}/%{name}/README
%{_datadir}/%{name}/TRANSLATIONS
%{_bindir}/fatrat
%{_bindir}/fatrat-conf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/data/btsearch/
%{_datadir}/%{name}/data/css/*
%{_datadir}/%{name}/data/btlinks.txt
%{_datadir}/%{name}/data/bttrackers.txt
%{_datadir}/%{name}/data/defaults.conf
%{_datadir}/%{name}/data/genssl.*
%{_datadir}/%{name}/data/mirrors.txt
%{_mandir}/man1/%{name}*
%{_datadir}/%{name}/data/remote/*

#----------------------------------------------------------------------------

%package devel
Summary:	Fatrat development files
Group:		Development/C++

%description devel
This package contains header files required for development.

%files devel
%{_includedir}/%{name}/*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}_%{beta}
%patch0 -p1

# remove Java web-interface applet
rm -rf data/remote/applet.html data/remote/applet/
%patch10 -p1

%build
%cmake_qt4 \
	-DCMAKE_EXE_LINKER_FLAGS="-lpthread -lssl -lcrypto -lboost_system -lboost_filesystem -lboost_thread -llog4cpp" \
	-DWITH_BITTORRENT=ON \
	-DWITH_CURL=ON \
	-DWITH_JABBER=ON \
	-DWITH_JPLUGINS=OFF \
	-DWITH_NLS=ON \
	-DWITH_WEBINTERFACE=ON

%make

%install
cp build/config.h .
%makeinstall_std -C build

%find_lang %{name} --with-qt


