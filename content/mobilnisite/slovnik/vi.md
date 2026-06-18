---
slug: "vi"
url: "/mobilnisite/slovnik/vi/"
type: "slovnik"
title: "VI – VCO Input Frequency"
date: 2025-01-01
abbr: "VI"
fullName: "VCO Input Frequency"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/vi/"
summary: "Vzorec používaný pro výpočet vstupní frekvence (Nu) pro napětím řízený oscilátor (VCO) v základnových stanicích UMTS, konkrétně pro pásmo FDD uplink. Zajišťuje přesnou generaci frekvence pro rádiové v"
---

VI je vstupní frekvence pro napětím řízený oscilátor (VCO) v základnové stanici UMTS, vypočítávaná pro zajištění přesného rádiového vysílání v uplinku na základě kmitočtu nosné.

## Popis

VI, neboli [VCO](/mobilnisite/slovnik/vco/) Input Frequency (vstupní frekvence VCO), je technický parametr definovaný ve specifikacích 3GPP, konkrétně v TS 25.141, pro testování shody základnových stanic UMTS. Představuje vypočítanou vstupní frekvenci, označovanou jako Nu, pro napětím řízený oscilátor (VCO) používaný v obvodech generování frekvence vysílače základnové stanice. Vzorec je dán jako Nu = 5 * (FUL – 670,1 MHz), kde FUL je kmitočet nosné uplinku v MHz pro režim Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)). Tento výpočet je klíčový pro zajištění, že VCO pracuje na správné frekvenci pro generování požadovaného rádiového signálu pro uplink, což je zásadní pro udržení přesnosti signálu a shody s regulatorními požadavky.

V architektuře základnové stanice UMTS je VCO klíčovou součástí frekvenčního syntezátoru, který generuje stabilní a přesné rádiové frekvence pro vysílání. Výstupní frekvence VCO je řízena vstupním napětím a parametr VI definuje konkrétní potřebnou vstupní frekvenci na základě přidělené nosné uplinku. Vzorec zohledňuje plánování kmitočtů a přidělování pásem v systémech UMTS FDD, kde se frekvence uplinku typicky nacházejí v konkrétních pásmech (např. kolem 1920-1980 MHz pro Pásmo I). Odečtením 670,1 MHz od FUL a vynásobením pěti výpočet převádí kmitočet nosné na mezifrekvenci vhodnou pro konstrukci VCO, což usnadňuje efektivní frekvenční syntézu a snižuje fázový šum.

Úloha VI v síti spočívá v zajištění, aby základnové stanice generovaly přesné frekvence pro uplink, což je zásadní pro správnou komunikaci s uživatelským zařízením (UE). Nepřesná generace frekvence může vést k rušení, snížení kvality signálu a nesplnění požadavků na využití spektra. Parametr VI se používá během testování a kalibrace základnových stanic k ověření, že obvody generování frekvence splňují standardy 3GPP. Je součástí širší sady testů shody, které zajišťují výkon základnové stanice, včetně výstupního výkonu, frekvenční stability a přesnosti modulace. Standardizací tohoto výpočtu umožňuje 3GPP konzistentní implementaci napříč různými výrobci základnových stanic, čímž podporuje interoperabilitu a spolehlivý provoz sítě.

## K čemu slouží

Parametr VI byl zaveden, aby řešil potřebu přesného generování frekvence v základnových stanicích UMTS, zejména pro přenosy [FDD](/mobilnisite/slovnik/fdd/) uplink. V raných mobilních sítích byla přesnost frekvence klíčová pro zamezení rušení a efektivní využití spektra, ale s vývojem sítí směrem ke 3G, širším šířkám pásma a vyšším přenosovým rychlostem se požadavky na frekvenční stabilitu staly přísnějšími. Vzorec Nu = 5 * (FUL – 670,1 MHz) poskytuje standardizovanou metodu pro výpočet vstupní frekvence [VCO](/mobilnisite/slovnik/vco/), která zajišťuje, že základnové stanice mohou generovat správný kmitočet nosné uplinku bez ohledu na konkrétní přidělené pásmo nebo kanál. Tím se řeší problém frekvenčního driftu a nepřesností, které by mohly vzniknout z odchylek v konstrukci oscilátoru nebo vlivem podmínek prostředí.

Historicky je vývoj VI spojen se standardizací UMTS v 3GPP Release 6, která zahrnovala podrobné specifikace pro testování shody základnových stanic. Předtím mohly být metody generování frekvence proprietární nebo méně rigorózně definované, což vedlo k potenciálním nekonzistencím mezi různými modely základnových stanic. Zavedení VI jako součásti TS 25.141 poskytlo jasný matematický vztah mezi kmitočtem nosné uplinku a vstupem VCO, což umožnilo výrobcům navrhovat frekvenční syntezátory, které jsou přesné a zároveň shodné se standardy 3GPP. To bylo motivováno potřebou podpory globálního roamingu a interoperability, protože sítě UMTS byly nasazovány po celém světě s různými kmitočtovými pásmy.

Dále VI řeší omezení starších přístupů, kde kalibrace frekvence mohla vyžadovat ruční nastavení nebo složité ladící obvody. Zahrnutím tohoto výpočtu do konstrukce základnové stanice se zjednodušuje proces frekvenční syntézy a snižuje se riziko lidské chyby. Použití konkrétního posunu (670,1 MHz) a násobitele (5) je optimalizováno pro typické rozsahy frekvencí používané v UMTS FDD, což zajišťuje, že VCO pracuje ve svém optimálním výkonovém rozsahu. To zvyšuje celkovou spolehlivost základnové stanice a přispívá k lepšímu výkonu sítě a uživatelskému zážitku. V následujících vydáních byl parametr VI zachován jako součást specifikací UMTS, což odráží jeho důležitost pro zajištění frekvenční přesnosti i při vývoji sítí směrem ke 4G a 5G.

## Klíčové vlastnosti

- Standardizovaný vzorec pro výpočet vstupní frekvence VCO v UMTS FDD
- Založen na kmitočtu nosné uplinku (FUL) pro přesné generování frekvence
- Zajišťuje shodu s požadavky 3GPP na testování shody základnových stanic
- Podporuje přesnou frekvenční syntézu pro přenos uplink
- Usnadňuje interoperabilitu mezi různými výrobci základnových stanic
- Používá se při testování a kalibraci frekvenční stability základnové stanice

## Související pojmy

- [VCO – Voice Carry Over](/mobilnisite/slovnik/vco/)
- [FDD – Frequency Division Duplexing](/mobilnisite/slovnik/fdd/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [VI na 3GPP Explorer](https://3gpp-explorer.com/glossary/vi/)
