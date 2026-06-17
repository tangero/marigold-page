---
slug: "lis"
url: "/mobilnisite/slovnik/lis/"
type: "slovnik"
title: "LIS – Location Information Server"
date: 2025-01-01
abbr: "LIS"
fullName: "Location Information Server"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lis/"
summary: "Location Information Server (LIS) je síťová entita, která poskytuje informace o poloze uživatelského zařízení (UE) autorizovaným aplikacím. Je klíčovou součástí pro služby založené na poloze (LBS) a t"
---

LIS je síťová entita, která poskytuje polohu uživatelského zařízení (User Equipment) autorizovaným aplikacím pro služby jako tísňové volání nebo služby založené na poloze, přičemž polohu určuje různými metodami a poskytuje ji prostřednictvím standardizovaných rozhraní.

## Popis

Location Information Server (LIS) je funkční entita jádra sítě v architektuře 3GPP pro poskytování služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)). Definována napříč specifikacemi jako TS 23.868 (pro požadavky služby), TS 25.414 (pro rozhraní UTRAN Iu) a TS 36.855 (pro určování polohy v LTE), je zodpovědná za správu požadavků na polohu, určení geografické polohy UE a doručení této informace autorizovaným klientům, známým jako LCS klienti. Těmito klienty mohou být interní síťové entity (např. pro zákonný odposlech) nebo externí aplikační servery třetích stran (např. pro navigační služby).

Architektonicky je LIS často realizována prostřednictvím komponent, jako je Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) a Serving Mobile Location Centre (SMLC). GMLC funguje jako brána, která zpracovává autentizaci, autorizaci a kontroly soukromí pro požadavky na polohu od externích klientů a směruje požadavky na příslušný síťový uzel. SMLC (nebo Evolved SMLC - [E-SMLC](/mobilnisite/slovnik/e-smlc/) v LTE) je entita, která skutečně provádí nebo koordinuje výpočet polohy. Vybere metodu určování polohy (např. [A-GNSS](/mobilnisite/slovnik/a-gnss/), [OTDOA](/mobilnisite/slovnik/otdoa/), [E-CID](/mobilnisite/slovnik/e-cid/)), komunikuje s UE a přístupovou sítí pro získání měření a vypočítá konečný odhad polohy.

LIS funguje prostřednictvím standardizované sekvence. LCS klient odešle požadavek na polohu do GMLC. GMLC autentizuje klienta a určí obsluhující síťový uzel UE (např. [MSC](/mobilnisite/slovnik/msc/) nebo [MME](/mobilnisite/slovnik/mme/)). Poté předá požadavek tomuto uzlu, který zapojí SMLC/E-SMLC. SMLC zahájí proceduru určování polohy s UE prostřednictvím rádiové přístupové sítě (např. přes LIRF v UTRAN nebo přímo přes LPP v LTE). UE může poskytnout měření (pro síťový výpočet) nebo dokonce vypočítanou polohu (pro terminálový výpočet). SMLC naformátuje odhad polohy (např. zeměpisná šířka, délka, nejistota) a odešle jej zpět řetězcem do GMLC, který jej nakonec doručí žádajícímu LCS klientovi, často s využitím protokolu Open Mobile Alliance (OMA) Mobile Location Protocol (MLP).

Její role je klíčová pro širokou škálu služeb. Pro tísňové služby musí poskytnout rychlou a přesnou polohu místům příjmu tísňových volání (PSAP). Pro komerční služby umožňuje aplikace jako sledování vozového parku, reklamu založenou na poloze a funkce sociálních sítí. Architektura LIS zajišťuje vynucení kontrol soukromí, takže poloha uživatele je zveřejněna pouze se souhlasem nebo na základě zákonného mandátu, a podporuje různé parametry kvality služby (QoS), jako je doba odezvy a přesnost požadovaná různými aplikacemi.

## K čemu slouží

Location Information Server byl vyvinut, aby poskytl standardizovanou, škálovatelnou a bezpečnou platformu pro poskytování informací o poloze v celulárních sítích. Před jeho formalizací v 3GPP byly služby určování polohy často proprietární nebo omezeného rozsahu. Architektura LIS vytvořila jednotný rámec, který oddělil funkci určování polohy od aplikací, které ji spotřebovávají, což umožnilo široký ekosystém služeb založených na poloze.

Řeší problém, jak efektivně a spolehlivě určit polohu mobilního zařízení a zpřístupnit ji autorizovaným subjektům. Tím se řeší jak regulační podněty, jako je Enhanced 911 (E-911) v USA a E-112 v Evropě, které nařizují poskytnutí polohy volajícího pro tísňové služby, tak komerční příležitosti na rostoucím trhu LBS. LIS poskytuje potřebná rozhraní, mechanismy ochrany soukromí a servisní logiku pro podporu těchto různorodých případů užití.

Motivace pro jeho vytvoření pramenila ze sbližování mobilní komunikace a technologií určování polohy (jako je GPS) na konci 90. let a počátkem 21. století. 3GPP uznala potřebu architektonického rámce, který by mohl podporovat více technologií určování polohy (síťové, na straně terminálu), integrovat se s prvky jádra sítě pro správu účastníků a zpřístupňovat polohu prostřednictvím standardních protokolů za účelem podpory vývoje aplikací. LIS prostřednictvím komponent, jako je GMLC a SMLC, tuto potřebu naplnila a stanovila základ pro všechny následné služby určování polohy v 3GPP.

## Klíčové vlastnosti

- Poskytuje geografickou polohu UE autorizovaným LCS klientům prostřednictvím standardizovaných rozhraní (např. OMA MLP)
- Podporuje více metod určování polohy včetně A-GNSS, OTDOA a Enhanced Cell ID
- Vynucuje zásady ochrany soukromí a autorizace pro přístup k poloze
- Architektonicky se skládá z bránových (GMLC) a výpočetních (SMLC/E-SMLC) funkcí
- Integruje se s jádrem sítě (HLR/HSS, MME) pro informace o účastníkovi a relaci
- Poskytuje polohu se specifikovanými parametry kvality služby (QoS), jako je přesnost a doba odezvy

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TS 23.868** (Rel-9) — Study on IMS Emergency Calls
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study

---

📖 **Anglický originál a plná specifikace:** [LIS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lis/)
