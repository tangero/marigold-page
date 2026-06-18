---
slug: "pbp"
url: "/mobilnisite/slovnik/pbp/"
type: "slovnik"
title: "PBP – Paging Block Periodicity"
date: 2025-01-01
abbr: "PBP"
fullName: "Paging Block Periodicity"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pbp/"
summary: "Parametr v systémech GSM a UMTS, který definuje časový interval mezi po sobě jdoucími stránkovacími bloky na kanálu řídicího vysílání (broadcast control channel). Řídí, jak často mobilní zařízení nasl"
---

PBP je parametr v systémech GSM a UMTS, který definuje časový interval mezi po sobě jdoucími stránkovacími bloky na kanálu řídicího vysílání (broadcast control channel), čímž vyvažuje životnost baterie a zpoždění při sestavování hovoru.

## Popis

Periodicita stránkovacích bloků (Paging Block Periodicity, PBP) je síťový parametr definovaný ve specifikacích 3GPP, včetně TS 21.905, používaný v GSM a UMTS rádiových přístupových sítích pro správu procesu stránkování mobilních zařízení v klidovém režimu. Určuje periodicitu, vyjádřenou v násobcích multiframů nebo časových jednotek, s jakou jsou stránkovací bloky vysílány na kanálu řídicího vysílání (Broadcast Control Channel, [BCCH](/mobilnisite/slovnik/bcch/)) nebo na stránkovacím kanálu (Paging Channel, [PCH](/mobilnisite/slovnik/pch-text-pch/)). Každému mobilnímu zařízení je na základě jeho identifikátoru (např. [IMSI](/mobilnisite/slovnik/imsi/)) přiřazena stránkovací skupina a zařízení se probouzí ke sledování stránkovacích zpráv pouze během svých určených stránkovacích bloků, které se opakují v intervalech daných PBP. Tento mechanismus umožňuje zařízením šetřit energii baterie přechodem do režimu spánku mezi stránkovacími příležitostmi, a zároveň zajišťuje, že je lze dosáhnout pro příchozí hovory nebo zprávy.

Z architektonického hlediska je PBP konfigurován operátorem sítě a vysílán v systémových informačních zprávách, jako jsou data BCCH v GSM nebo hlavní informační blok (Master Information Block, [MIB](/mobilnisite/slovnik/mib/)) v UMTS. Funguje ve spojení s dalšími parametry stránkování, jako je počet stránkovacích bloků na interval a algoritmus pro výpočet stránkovací skupiny. Když síť potřebuje zařízení stránkovat – například pro zahájení hovoru směrovaného k mobilnímu účastníkovi – odešle stránkovací zprávu v příslušném bloku na základě stránkovací skupiny zařízení a hodnoty PBP. Přijímač zařízení je synchronizován s tímto rozvrhem a probouzí se v přesně stanovených časech, aby zkontroloval zprávy. Pokud není zjištěno žádné stránkování, vrací se do režimu spánku, což významně prodlužuje životnost baterie.

Hodnota PBP představuje kompromis: kratší periody snižují zpoždění při sestavování hovoru, ale zvyšují spotřebu energie, zatímco delší periody šetří baterii na úkor latence. V GSM je PBP často vyjádřeno v násobcích 51-multiframů (např. 2, 4, 6 multiframů), což odpovídá intervalům přibližně 0,47 až 1,4 sekundy. V UMTS souvisí s časováním kanálu indikátoru stránkování (Paging Indicator Channel, [PICH](/mobilnisite/slovnik/pich/)) a stránkovacího kanálu ([PCH](/mobilnisite/slovnik/pch/)). PBP je klíčové pro efektivitu sítě, protože určuje kapacitu stránkování – počet zařízení, která lze v daném časovém rámci stránkovat. Optimalizací PBP mohou operátoři vyvažovat kvalitu služeb s výkonem baterie zařízení, což bylo zvláště důležité pro rané mobilní sítě a stále je relevantní pro IoT zařízení v pozdějších technologiích.

## K čemu slouží

PBP bylo zavedeno, aby řešilo základní výzvu efektivního dosažení mobilních zařízení v klidovém režimu bez vybíjení jejich baterií. V raných celulárních systémech, jako je GSM, před standardizací stránkovací periody musela zařízení možná neustále monitorovat kanály, což vedlo k nepraktické životnosti baterie. Release 4 3GPP formalizoval PBP jako součást struktury stránkovacího kanálu a poskytl konfigurovatelný parametr pro řízení toho, jak často zařízení naslouchají síťovým upozorněním.

Vytvoření PBP bylo motivováno potřebou škálovat sítě pro masové přijetí při zachování uživatelského zážitku. Řeší problém vyvážení času potřebného k sestavení hovoru a spotřeby energie zařízení, což bylo klíčové pro úspěch mobilních telefonů. Tím, že umožnilo zařízením přecházet do režimu spánku na předvídatelné intervaly, PBP prodloužilo životnost baterie z hodin na dny, což byl klíčový prodejní argument pro spotřebitele. Historicky, jak se sítě vyvíjely, aby podporovaly více uživatelů, PBP také pomáhalo zvládat přetížení stránkovacího kanálu rozložením probouzení zařízení v čase. Jeho standardizace umožnila interoperabilitu mezi zařízeními a sítěmi a zajistila konzistentní chování. PBP zůstává relevantní v legacy systémech a ovlivňuje pozdější mechanismy úspory energie v LTE a 5G, což dokládá jeho základní roli v mobilních komunikacích.

## Klíčové vlastnosti

- Definuje časový interval mezi přenosy stránkovacích bloků na kanálech řídicího vysílání
- Umožňuje mobilním zařízením přecházet do režimu spánku za účelem úspory energie baterie
- Konfigurovatelné operátory sítě pro vyvážení latence a spotřeby energie
- Integrováno s přiřazením stránkovací skupiny pro efektivní adresování zařízení
- Vysíláno v systémových informacích pro synchronizaci zařízení
- Podporuje škálovatelnost rozložením stránkovací zátěže v časových intervalech

## Související pojmy

- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [PBP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pbp/)
