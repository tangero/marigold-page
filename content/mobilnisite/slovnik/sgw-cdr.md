---
slug: "sgw-cdr"
url: "/mobilnisite/slovnik/sgw-cdr/"
type: "slovnik"
title: "SGW-CDR – Serving Gateway Call Detail Record"
date: 2025-01-01
abbr: "SGW-CDR"
fullName: "Serving Gateway Call Detail Record"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sgw-cdr/"
summary: "SGW-CDR je formátovaný datový záznam generovaný Serving Gateway (SGW), který detailně popisuje využití prostředků pro přenosové spojení IP-CAN (IP Connectivity Access Network). Je klíčovou součástí pr"
---

SGW-CDR je formátovaný záznam generovaný Serving Gateway (SGW), který detailně popisuje využití prostředků, jako je objem dat a doba trvání, pro přenosové spojení IP-CAN (IP Connectivity Access Network). Používá se pro účtování a analýzu sítě.

## Popis

Serving Gateway Call Detail Record (SGW-CDR) je specifický typ záznamu o účtovacích datech (Charging Data Record, [CDR](/mobilnisite/slovnik/cdr/)) generovaný funkcí Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) v síti 3GPP. Jeho primárním účelem je zaznamenávat informace související s účtováním pro relaci přenosového spojení [IP-CAN](/mobilnisite/slovnik/ip-can/) (IP Connectivity Access Network) uživatele. SGW, která vystupuje jako funkce spouštějící účtování (Charging Trigger Function, [CTF](/mobilnisite/slovnik/ctf/)), shromažďuje data o využití a formátuje je do SGW-CDR podle pravidel poskytnutých Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) nebo Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)). Tento záznam je následně přenesen do funkce Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) nebo přímo do fakturačního systému pro další zpracování. Vytváření a obsah SGW-CDR je standardizován v dokumentu 3GPP TS 32.251, který definuje architekturu a principy účtování.

SGW-CDR obsahuje komplexní sadu polí popisujících relaci přenosového spojení. Mezi klíčové datové body patří [IMSI](/mobilnisite/slovnik/imsi/) a MSISDN účastníka, adresy SGW a PGW použité pro relaci, název přístupového bodu (Access Point Name, APN) a typ technologie rádiového přístupu (Radio Access Technology, RAT) (např. LTE, NR). Nejdůležitější je, že zaznamenává kvantifikovatelné metriky využití: celkový objem přenesených uživatelských dat ve směru uplink a downlink, dobu trvání relace (čas zahájení a ukončení) a parametry QoS, jako je Allocation and Retention Priority (ARP) a Guaranteed Bit Rate (GBR), pokud jsou použity. Záznam také obsahuje identifikátory pro účtování, důvod ukončení relace a případné použité účtovací charakteristiky.

Generování SGW-CDR je spuštěno specifickými událostmi během životního cyklu přenosového spojení. Mezi tyto spouštěče patří počáteční vytvoření přenosového spojení, jakákoli modifikace jeho parametrů QoS (což může vést k uzavření průběžného CDR a otevření nového) a konečné ukončení relace přenosového spojení. U dlouhotrvajících relací, aby se zabránilo ztrátě dat a zvládla se velikost záznamů, může SGW generovat více dílčích SGW-CDR na základě časových limitů, limitů objemu dat nebo změn tarifního času. Tyto dílčí záznamy jsou korelovány pomocí společného čísla posloupnosti záznamů (Record Sequence Number). SGW-CDR spolupracuje s CDR z jiných síťových funkcí, jako je PGW-CDR, aby poskytl úplný obraz o datové relaci uživatele pro přesné účtování a síťové analýzy.

## K čemu slouží

SGW-CDR existuje proto, aby umožnil přesné a spolehlivé účtování za služby mobilních dat. V počátcích mobilních dat byla možná jednoduchá fakturační schémata, ale s vývojem služeb a zavedením Evolved Packet System (EPS) ve verzi 3GPP Release 8 se stala podrobnější a flexibilnější fakturace komerční nutností. Operátoři potřebovali účtovat na základě objemu dat, doby trvání relace, typu služby (pomocí APN) a kvality služby, což vyžadovalo detailní záznamy ze síťových uzlů, které zpracovávají uživatelský provoz.

SGW-CDR řeší problém přiřazení využití prostředků konkrétnímu účastníkovi a službě. SGW je klíčový uzel, který vidí veškerý uživatelský provoz pro UE ve své obslužné oblasti, což z něj činí ideální místo pro měření spotřeby na úrovni přenosového spojení. Před standardizovanými formáty CDR ztěžovala proprietární evidence interoperabilitu mezi síťovým vybavením a fakturačními systémy. Standardizace SGW-CDR v TS 32.251 zajistila kompatibilitu mezi výrobci a umožnila vytvoření konsolidovaných fakturačních systémů, které dokážou zpracovávat záznamy z různých síťových prvků. Podporuje jak offline účtování (post-paid fakturace), tak prostřednictvím interakce s OCS online účtování (pre-paid / kontrola kreditu v reálném čase). Toto podrobné účtování je základním kamenem obchodních modelů operátorů mobilních sítí.

## Klíčové vlastnosti

- Zaznamenává data o využití specifická pro přenosové spojení IP-CAN (objem, doba trvání)
- Obsahuje identifikátory účastníka (IMSI, MSISDN) a APN
- Eviduje parametry QoS, jako je ARP a GBR
- Podporuje generování dílčích CDR pro dlouhé relace
- Obsahuje typ RAT a informace o poloze uživatele
- Standardizovaný formát definovaný v 3GPP TS 32.251 pro interoperabilitu

## Související pojmy

- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)
- [PGW-CDR – P-GW (enhanced by FBC) generated – Charging Data Record](/mobilnisite/slovnik/pgw-cdr/)

## Definující specifikace

- **TS 32.251** (Rel-19) — PS Domain Charging Management

---

📖 **Anglický originál a plná specifikace:** [SGW-CDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/sgw-cdr/)
