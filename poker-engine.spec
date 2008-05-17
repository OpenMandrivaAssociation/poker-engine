%bcond_without  tests

Name:           poker-engine
Version:        1.2.0
Release:        %mkrel 1
Epoch:          0
Summary:        Python library that implements poker rules
Group:          Development/Python
License:        GPLv3+
URL:            http://pokersource.org/poker-engine/
Source0:        http://download.gna.org/pokersource/sources/poker-engine-%{version}.tar.gz
BuildRequires:  pypoker-eval-devel
BuildRequires:  python-devel
BuildRequires:  python-libxslt
BuildRequires:  rsync
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{epoch}:%{version}-%{release}-root

%description
This is a python library that implements poker rules according
to variants and betting structures specified in configuration files.
It designed to be used by a multiplayer poker server, a poker AI or a
poker client.

%package -n python-pokerengine
Summary:        Python library that implements poker rules
Group:          Development/Python
Provides:       %{name} = %{epoch}:%{version}-%{release}
Requires:       pypoker-eval
Requires:       rsync

%description -n python-pokerengine
This is a python library that implements poker rules according
to variants and betting structures specified in configuration files.
It designed to be used by a multiplayer poker server, a poker AI or a
poker client.

%package -n python-pokerengine-devel
Summary:        Poker rule implementation library development files
Group:          Development/Python
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}
Requires:       python-pokerengine = %{epoch}:%{version}-%{release}
Requires:       pypoker-eval-devel

%description -n python-pokerengine-devel
This package contains files required to build applications that use
poker-engine.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%if %with tests
%check
%{make} check
%endif

%clean
%{__rm} -rf %{buildroot}

%files -n python-pokerengine
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_mandir}/man8/*.8*
%{_sbindir}/pokerconfigupgrade
%{_datadir}/%{name}/conf/*.xml
%{python_sitelib}/pokerengine
%config(noreplace) %{_sysconfdir}/%{name}/*
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/poker-engine.mo

%files -n python-pokerengine-devel
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/%{name}.pc
