---
slug: "spt"
url: "/mobilnisite/slovnik/spt/"
type: "slovnik"
title: "SPT – Service Point Trigger"
date: 2025-01-01
abbr: "SPT"
fullName: "Service Point Trigger"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/spt/"
summary: "Logický bod v rámci vykonávání servisní logiky (např. v IMS Application Server nebo službě CAMEL), kde se vyhodnocuje spouštěcí podmínka. Určuje, zda se má vyvolat specifická servisní logika, což umož"
---

SPT je logický bod v rámci vykonávání servisní logiky, kde se vyhodnocuje spouštěcí podmínka, aby se určilo, zda se má vyvolat specifické, dynamické chování služby na základě stavu účastníka nebo síťových událostí.

## Popis

Service Point Trigger (SPT) je základní koncept v architektuře služeb inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) a IP Multimedia Subsystem (IMS), definovaný ve specifikacích 3GPP pro Customised Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)) a IMS Service Control ([ISC](/mobilnisite/slovnik/isc/)). Představuje specifickou, přesně definovanou událost nebo podmínku během zpracování hovoru, relace nebo interakce s účastníkem, kterou lze použít ke 'spuštění' vyvolání externí servisní logiky. Lze si jej představit jako háček nebo rozhodovací bod zabudovaný do základního modelu stavu hovoru/relace. Když síťový prvek (jako Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) nebo Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/))) dosáhne SPT, vyhodnotí, zda jsou pro konkrétního účastníka splněny nakonfigurované spouštěcí podmínky. Pokud ano, pozastaví běžné zpracování a předá řízení relace externímu aplikačnímu serveru ([AS](/mobilnisite/slovnik/as/)), jako je CAMEL Service Environment ([CSE](/mobilnisite/slovnik/cse/)) nebo IMS AS, který vykoná přizpůsobenou servisní logiku.

SPT jsou definovány v servisním profilu účastníka, který je stažen do síťového prvku (např. z [HSS](/mobilnisite/slovnik/hss/)/HLR). Tento profil obsahuje sadu Initial Filter Criteria (iFC) v IMS nebo CAMEL Subscription Information (CSI) v okruhově přepínaných doménách. Každé kritérium zahrnuje jeden nebo více SPT a adresu AS, na kterou se má obrátit, pokud je podmínka splněna. SPT může být založeno na různých aspektech: Request-URI SIP zprávy, SIP metodě (INVITE, MESSAGE, SUBSCRIBE), přítomnosti nebo hodnotě konkrétních SIP hlaviček, případu relace (vycházející/terminující), registračním stavu účastníka nebo zahrnutém typu média. Například SPT může být definováno pro událost 'SIP Method je MESSAGE' a 'Request-URI obsahuje 'conference''. Když uživatel pošle zprávu na konferenční URI, S-CSCF narazí na tento SPT, vyhodnotí jej jako pravdivý a směruje MESSAGE na aplikační server pro zasílání zpráv.

Operace je sekvenční a založená na prioritách. Síťový prvek vyhodnocuje seznam spouštěčů (iFC) v definovaném pořadí priority. Když najde první podmínku SPT, která odpovídá, předá relaci příslušnému AS. AS poté vykoná svou servisní logiku, která může relaci upravit (např. přesměrování hovoru, přehrání oznámení, úprava hlaviček) a následně vrátí řízení zpět S-CSCF. S-CSCF pak může pokračovat ve vyhodnocování následujících spouštěčů. Tento mechanismus umožňuje skládání komplexních služeb z jednodušších stavebních bloků hostovaných na různých AS. Klíčovými komponentami jsou bod detekce spouštěče v síťovém prvku, profil filtračních kritérií účastníka a standardizované rozhraní (např. CAP, IMS ISC) k AS.

SPT jsou klíčovými prvky umožňujícími personalizaci služeb a poskytování služeb třetími stranami. Oddělují servisní logiku od funkcí přepínání/směrování v jádru sítě, což umožňuje služby vyvíjet a nasazovat nezávisle. Tato architektura je ústřední pro ekosystém služeb s přidanou hodnotou jak v zastaralých okruhově přepínaných sítích, tak v moderních sítích založených na IMS pro služby jako předplacené účtování, filtrování hovorů, překlad čísel, multimediální konference a instant messaging.

## K čemu slouží

Koncept Service Point Trigger vychází z principů inteligentní sítě (IN) přijatých 3GPP, primárně za účelem řešení problému monolitických, nepružných síťových ústředen. V tradiční telefonii vyžadovaly nové služby (jako přesměrování hovorů nebo předplacené) nákladné a časově náročné softwarové aktualizace ústředny od jediného dodavatele. To potlačovalo inovace a vedlo k dlouhým cyklům nasazování služeb. Architektura IN, a následně SPT v CAMEL a IMS, zavedla standardizovaný způsob externalizace servisní logiky, umožňující její umístění na samostatných, snadněji aktualizovatelných aplikačních serverech.

Primární problém, který SPT řeší, je umožnění dynamického, na účastníka specifického vyvolání služby bez nutnosti pevného zakódování logiky do každého síťového uzlu. Poskytují mechanismus pro 'servisní povědomí' v jádru sítě. Bez SPT by ústředna nebo S-CSCF neměla standardizovaný způsob, jak poznat, kdy přerušit své základní zpracování hovoru/relace, aby zapojila specializovanou službu. SPT definují 'kdy' a 'proč' na základě kombinace signalizace relace a profilu účastníka. To umožňuje hromadné přizpůsobení – kde každý účastník může mít jedinečnou sadu aktivních služeb – což je zásadní pro moderní telekomunikace.

Historicky byly SPT formalizovány v 3GPP s CAMEL pro GSM okruhově přepínané služby (počínaje Rel-4/5) za účelem umožnění operátorům specifických služeb, jako je předplacené roamování. Jejich role se stala ještě kritičtější se zavedením IMS v Rel-5, které používalo SIP jako protokol pro řízení relace. IMS potřebovalo flexibilní, SIP-aware spouštěcí mechanismus pro vybudování multimediální servisní vrstvy. SPT, jako součást Initial Filter Criteria, se staly základním kamenem IMS platformy pro poskytování služeb, umožňující konvergenci hlasových, video a messagingových služeb přes IP. Jsou i nadále nezbytné pro umožnění síťových API (jako CAPIF) a servisní expozice, propojující jádro sítě s aplikační vrstvou over-the-top řízeným způsobem.

## Klíčové vlastnosti

- Definuje specifické události nebo podmínky (SIP metody, URI, hlavičky) v průběhu relace, které mohou spustit externí servisní logiku.
- Konfigurováno na účastníka v servisních profilech (např. iFC v IMS) stažených z HSS.
- Umožňuje sekvenční, na prioritě založené vyhodnocení více spouštěčů pro řetězení služeb.
- Odděluje vykonávání služeb (na Application Serverech) od základního řízení relace (v CSCF/MSC).
- Podporuje jak okruhově přepínané (CAMEL), tak paketově přepínané (IMS) servisní architektury.
- Základní pro umožnění personalizovaných služeb s přidanou hodnotou, jako je předplacené, filtrování hovorů a multimediální konference.

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 29.562** (Rel-19) — HSS Services for IMS & GBA Interworking
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SPT na 3GPP Explorer](https://3gpp-explorer.com/glossary/spt/)
