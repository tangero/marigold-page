---
slug: "sc-rnti"
url: "/mobilnisite/slovnik/sc-rnti/"
type: "slovnik"
title: "SC-RNTI – Single Cell Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "SC-RNTI"
fullName: "Single Cell Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sc-rnti/"
summary: "Identifikátor specifický pro konkrétní uživatelské zařízení (UE), používaný pro plánování a signalizaci řídicích zpráv v rámci jedné buňky LTE. Umožňuje efektivní přidělování zdrojů pro uživatelská za"
---

SC-RNTI je identifikátor specifický pro konkrétní uživatelské zařízení (UE), používaný pro plánování a signalizaci řídicích zpráv v rámci jedné buňky LTE. Umožňuje efektivní přidělování zdrojů pro procedury, jako je náhodný přístup, bez nutnosti plnohodnotného C-RNTI.

## Popis

Single Cell Radio Network Temporary Identifier (SC-RNTI) je klíčový identifikátor v LTE rádiové přístupové síti (RAN), specificky definovaný v kontextu vrstvy [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control). Jedná se o 16bitovou hodnotu, podobně jako jiné typy [RNTI](/mobilnisite/slovnik/rnti/), kterou eNodeB používá k adresování konkrétního uživatelského zařízení (UE) na fyzickém kanálu pro řídicí přenosy v downlinku ([PDCCH](/mobilnisite/slovnik/pdcch/)) za účelem plánování zdrojů sdíleného kanálu pro uplink nebo downlink. Na rozdíl od Cell RNTI ([C-RNTI](/mobilnisite/slovnik/c-rnti/)), které je primárním identifikátorem pro UE v režimu [RRC](/mobilnisite/slovnik/rrc/)_CONNECTED a je specifické pro buňku, ale může být zachováno během předávání spojení, je SC-RNTI výslovně navrženo pro použití v rámci jedné konkrétní buňky. Jeho přidělení a použití jsou úzce spjaty se specifickými procedurami vrstvy MAC.

Operačně je SC-RNTI přiděleno UE ze strany eNodeB během konkrétních událostí. Primárním případem použití je procedura na náhodném přístupovém kanálu ([RACH](/mobilnisite/slovnik/rach/)) pro náhodný přístup s konkurencí. Když UE vysílá preambuli náhodného přístupu (Msg1), eNodeB odpoví odpovědí na náhodný přístup ([RAR](/mobilnisite/slovnik/rar/), Msg2) na [PDSCH](/mobilnisite/slovnik/pdsch/). Plánovací informace pro tuto RAR jsou indikovány na PDCCH adresované pomocí RA-RNTI, které je společné pro daný časově-frekvenční zdroj. Pro následné zprávy však, pokud jsou UE přidělovány zdroje pro Msg3 (první plánovaný uplinkový přenos obsahující identitu UE) nebo pro zprávu o časovém rozřešení konkurence, může eNodeB použít dočasné C-RNTI (které se po úspěšném rozřešení konkurence stává C-RNTI) nebo, v definovaných scénářích, SC-RNTI. Specifikace 3GPP (TS 36.321 pro MAC) detailně popisují přesné podmínky, za kterých je SC-RNTI použito pro adresování specifických řídicích prvků nebo dat vrstvy MAC.

Z architektonického hlediska se SC-RNTI nachází v podsložce MAC eNodeB a UE. Plánovač eNodeB používá hodnotu SC-RNTI ke skramblování bitů cyklického redundantního součtu (CRC) formátu řídicí informace pro downlink (DCI) vysílaného na PDCCH. UE kontinuálně monitoruje PDCCH pro formáty DCI skramblované pomocí RNTI, která je nakonfigurována sledovat. Když UE detekuje DCI s CRC skramblovaným jejím přiděleným SC-RNTI, ví, že přidružené povolení nebo přiřazení na PDSCH nebo PUSCH je určeno pro ni. Tento mechanismus umožňuje vysoce efektivní adresování konkrétního UE s nízkou režií bez nutnosti explicitního adresování vyšší vrstvou v každém přenosu. Jeho role je zvláště důležitá pro optimalizaci efektivity signalizace pro občasné nebo malé dávky dat, což pomáhá snižovat režii řídicích kanálů a spotřebu baterie UE.

## K čemu slouží

SC-RNTI bylo zavedeno, aby poskytlo zjednodušený, dočasný identifikátor pro efektivní správu rádiových zdrojů v rámci jedné buňky LTE, řešící specifické scénáře, kdy je plné, trvalé C-RNTI zbytečné nebo neefektivní. Před jeho explicitní definicí se používaly dočasné identifikátory, ale SC-RNTI formalizovalo jasný mechanismus pro operace v rámci jedné buňky. Primární problém, který řeší, je potřeba metody s nízkou režií pro plánování zdrojů pro UE během přechodných stavů nebo pro specifické procedury bez přidělení plných práv a trvalosti C-RNTI.

Historicky, jak se sítě LTE vyvíjely pro podporu obrovského počtu zařízení, včetně těch pro komunikaci typu stroj-stroj (MTC) a internet věcí (IoT), se optimalizace každého bitu řídicí signalizace stala prvořadou. Procedury jako náhodný přístup a přenos malých datových paketů jsou klíčové pro vstup do sítě a efektivní provoz. Používání vyhrazeného C-RNTI pro každou drobnou interakci by mohlo být plýtváním. SC-RNTI poskytuje střední cestu – identifikátor specifický pro UE, který síť může dočasně použít pro omezený účel v rámci jedné buňky, a poté jej může uvolnit. To je zvláště užitečné ve scénářích jako časný přenos dat nebo pro specifické řídicí prvky vrstvy MAC, kde je komunikační kontext omezený a předávání spojení není relevantní. Řeší tak omezení používání společných RNTI (jako RA-RNTI nebo P-RNTI) pro skupinové zprávy nebo vysílání, kterým chybí uživatelská specifičnost, a omezení neustálého používání C-RNTI, které předpokládá stabilnější RRC spojení a spotřebovává dlouhodobější identifikátorový zdroj v řídicích tabulkách eNodeB.

## Klíčové vlastnosti

- 16bitový identifikátor specifický pro UE pro adresování na PDCCH
- Používá se pro plánování pouze v rámci jedné buňky LTE
- Aplikováno v specifických procedurách vrstvy MAC, jako je náhodný přístup
- Umožňuje efektivní přidělování zdrojů pro přechodné stavy UE
- Snižuje režii řídicí signalizace ve srovnání s trvalým C-RNTI
- Skrambluje CRC formátů DCI pro povolení specifická pro UE

## Související pojmy

- [C-RNTI – Cell Radio Network Temporary Identifier](/mobilnisite/slovnik/c-rnti/)
- [RA-RNTI – Random Access Radio Network Temporary Identifier](/mobilnisite/slovnik/ra-rnti/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SC-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sc-rnti/)
