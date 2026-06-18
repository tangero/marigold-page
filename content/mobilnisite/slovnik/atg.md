---
slug: "atg"
url: "/mobilnisite/slovnik/atg/"
type: "slovnik"
title: "ATG – Aircraft Mounted UE"
date: 2025-01-01
abbr: "ATG"
fullName: "Aircraft Mounted UE"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/atg/"
summary: "ATG označuje uživatelské zařízení (UE) umístěné na letadle, které umožňuje připojení během letu prostřednictvím pozemních 5G sítí. Umožňuje cestujícím a posádce přístup ke službám mobilního širokopásm"
---

ATG je uživatelské zařízení (User Equipment) umístěné na palubě letadla, které umožňuje připojení k pozemním 5G sítím během letu pro služby mobilního širokopásmového přístupu.

## Popis

ATG (Aircraft Mounted UE) je specializované uživatelské zařízení integrované do palubní avioniky nebo trupu letadla, navržené pro připojení k pozemním 5G New Radio (NR) základnovým stanicím (gNB) z velkých výšek. Na rozdíl od konvenčních pozemních UE pracuje ATG v jedinečném leteckém prostředí charakterizovaném vysokou mobilitou (rychlosti až 1000 km/h), značnou nadmořskou výškou (typicky 3–12 km nad zemí) a rozšířenými podmínkami přímé viditelnosti pro šíření signálu. Zařízení UE je umístěno vně nebo uvnitř letadla s anténami optimalizovanými pro aerodynamickou účinnost a vysokofrekvenční výkon a připojuje se k 5G síti jako standardní UE, avšak s vylepšenými protokoly pro správu mobility a rádiových zdrojů, které zvládají dynamický letecký scénář.

Architektura zahrnuje komunikaci ATG UE přímo s pozemními gNB, které jsou součástí rádiové přístupové sítě (RAN). Připojení využívá stávající kmitočtová pásma 5G NR, včetně středního pásma (např. 3,5 GHz) a potenciálně i vysokofrekvenčního spektra, s konkrétními vylepšeními definovanými ve specifikacích 3GPP pro podporu leteckého spoje. Mezi klíčové technické aspekty patří úpravy beamformingu s ohledem na náklon a klopení letadla, kompenzace Dopplerova jevu pro pohyb vysokou rychlostí a vylepšené postupy předávání spojení pro zajištění konektivity napříč širokou geografickou oblastí pokrytou více pozemními buňkami. ATG UE komunikuje s palubními systémy letadla, aby poskytovalo připojení k zařízením cestujících prostřednictvím palubního přístupového bodu Wi-Fi nebo přímo k avionice pro provozní data.

Z pohledu sítě je ATG UE považováno za vysoce mobilní UE v rámci 5G systému. RAN implementuje specifické algoritmy pro výběr a převýběr buňky s ohledem na rozšířený dosah buňky a potenciální interference s pozemními UE. Jádrová síť (5GC) spravuje relaci a mobilitu ATG UE a uplatňuje zásady kvality služeb (QoS) přizpůsobené scénářům za letu, jako je upřednostňování komunikací souvisejících s bezpečností. Specifikace jako TS 38.876 definují požadavky na výkon a testovací podmínky pro ATG, což zajišťuje spolehlivý provoz v leteckém prostředí.

Úlohou ATG v síti je rozšířit pokrytí pozemní 5G sítě do vzdušné oblasti, což umožňuje služby jako širokopásmový internet, hlasové služby a přenos videa v reálném čase pro cestující, a také podporuje provozní potřeby letectví, jako je monitorování stavu letadla a komunikace pro řízení letového provozu. Doplněk ATG k jiným řešením letecké konektivity, jako jsou satelitní systémy, spočívá v nabídnutí vyšší kapacity a nižší latence nad obydlenými pevninskými oblastmi, kde je infrastruktura 5G hustá. Integrace následuje rámec neterestrických sítí ([NTN](/mobilnisite/slovnik/ntn/)) podle 3GPP, ale zaměřuje se na pozemní spoje, což vyžaduje koordinaci mezi operátory mobilních sítí a leteckými úřady pro správu spektra a bezpečnostních předpisů.

## K čemu slouží

Technologie ATG byla zavedena, aby řešila rostoucí poptávku po vysoce kvalitním připojení během letu ([IFC](/mobilnisite/slovnik/ifc/)) s nízkou latencí, které stávající řešení, založená primárně na satelitní komunikaci, nedokáží uspokojivě poskytnout. Satelitní systémy často trpí omezenou šířkou pásma, vysokou latencí (zejména na geostacionárních drahách) a vysokými náklady, což omezuje uživatelský zážitek u aplikací náročných na přenosovou kapacitu, jako je streamování videa a videokonference během letů. Rozšíření 5G sítí s hustou pozemní infrastrukturou představovalo příležitost využít je pro letecké pokrytí a nabídnout tak komplementární cestu k zajištění vyšší kapacity a výkonu nad pevninskými trasami.

Vznik ATG ve 3GPP Release 18 byl motivován potřebou leteckého průmyslu po plynulém připojení, které podporuje jak zábavu cestujících, tak provozní efektivitu. Předchozí přístupy spoléhaly na ad-hoc modifikace protokolů pro pozemní UE, které byly nedostatečné pro jedinečné výzvy letecké mobility, jako jsou rychlá předávání spojení, Dopplerovy jevy a správa interference ve velkých výškách. Standardizací ATG jako typu UE umožňuje 3GPP interoperabilitu mezi leteckým zařízením a globálními 5G sítěmi, čímž snižuje náklady na nasazení a podporuje inovace v leteckých službách.

ATG řeší problém rozšíření pozemního mobilního širokopásmového přístupu na letadla bez nutnosti zcela nové síťové infrastruktury, neboť využívá stávající investice do 5G RAN. Řeší omezení, jako jsou mezery v pokrytí nad odlehlými oblastmi, potenciální integrací s řešeními [NTN](/mobilnisite/slovnik/ntn/), ale jeho primární zaměření je na vylepšení konektivity nad městskými a příměstskými koridory, kde je nasazení 5G rozsáhlé. Tato standardizace zajišťuje, že zařízení ATG splňují přísná kritéria výkonu a bezpečnosti, jak je uvedeno ve specifikacích jako TS 38.141 pro [RF](/mobilnisite/slovnik/rf/) shodu, což usnadňuje regulační schválení a široké přijetí v komerčním letectví.

## Klíčové vlastnosti

- Podpora vysokorychlostní mobility až do 1000 km/h
- Vylepšené beamformingové a anténní návrhy pro šíření signálu ve vzduchu
- Mechanismy kompenzace Dopplerova posunu na fyzické vrstvě
- Optimalizované postupy předávání spojení pro nepřetržité připojení napříč pozemními buňkami
- Integrace s palubními systémy letadla pro data cestujících a provozní data
- Soulad s leteckými bezpečnostními a regulačními požadavky

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)

## Definující specifikace

- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TR 38.876** (Rel-18) — Technical Report on Air-to-Ground Network for NR

---

📖 **Anglický originál a plná specifikace:** [ATG na 3GPP Explorer](https://3gpp-explorer.com/glossary/atg/)
