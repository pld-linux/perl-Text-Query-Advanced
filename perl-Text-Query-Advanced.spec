%include	/usr/lib/rpm/macros.perl
Summary:	Text-Query-Advanced perl module
Summary(pl):	Modu³ perla Text-Query-Advanced
Name:		perl-Text-Query-Advanced
Version:	0.05
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Query-Advanced-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Query-Advanced - matches text against Boolean expression.

%description -l pl
Text-Query-Advanced - wyszukuje tekst stosuj±c operatory logiczne.

%prep
%setup -q -n Text-Query-Advanced-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/Query/Advanced.pm
%{_mandir}/man3/*
