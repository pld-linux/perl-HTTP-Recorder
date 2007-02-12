#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTTP
%define		pnam	Recorder
Summary:	Proxy HTTP request and save it to Web::Mechanize scripts
Summary(pl.UTF-8):   Pośredniczenie w dialogu HTTP i zapisywanie go jako skrypt Web::Mechanize
Name:		perl-%{pdir}-%{pnam}
Version:	0.05
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2c167d06509620921e4d417ce9354a7
URL:		http://search.cpan.org/dist/HTTP-Recorder/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTTP-Request-Params
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%endif
Requires:	perl-HTTP-Proxy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a browser-independent recorder for recording interactions with
web sites.

%description -l pl.UTF-8
Niezależne od przeglądarki narzędzie do zapisywania dialogu ze
stronami WWW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/HTTP/*.pm
%{perl_vendorlib}/HTTP/Recorder
%{_mandir}/man3/*
