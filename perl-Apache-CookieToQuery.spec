#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	CookieToQuery
Summary:	Apache::CookieToQuery - rewrite query string by adding cookie information
Summary(pl):	Apache::CookieToQuery - przepisywanie zapytañ przez dodawanie informacji o cookie
Name:		perl-Apache-CookieToQuery
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a8911d246f918186fbe3703ff04681c
BuildRequires:	perl-devel >= 1:5.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	apache1-mod_perl
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will aid in adding cookie information to your query
strings so that CGI scripts or handlers underneath can have immediate
benefit.

%description -l pl
Ten modu³ pomaga w dodawaniu informacji o ciasteczkach do ³añcuchów
zapytañ, co daje bezpo¶rednie korzy¶ci skryptom lub procedurom obs³ugi
CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Apache/*.pm
%{_mandir}/man3/*
