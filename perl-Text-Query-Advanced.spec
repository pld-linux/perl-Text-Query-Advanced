%include	/usr/lib/rpm/macros.perl
Summary:	Text-Query-Advanced perl module
Summary(pl):	Modu� perla Text-Query-Advanced
Name:		perl-Text-Query-Advanced
Version:	0.03
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Query-Advanced-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Text-Query-Advanced - matches text against Boolean expression.

%description -l pl
Text-Query-Advanced - wyszukuje tekst stosuj�c operatory logiczne.

%prep
%setup -q -n Text-Query-Advanced-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/Query/Advanced
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,readme}.gz

%{perl_sitelib}/Text/Query/Advanced.pm
%{perl_sitearch}/auto/Text/Query/Advanced

%{_mandir}/man3/*
