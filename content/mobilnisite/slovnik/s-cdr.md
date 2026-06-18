---
slug: "s-cdr"
url: "/mobilnisite/slovnik/s-cdr/"
type: "slovnik"
title: "S-CDR – SGSN (IP-CAN bearer) generated – Charging Data Record"
date: 2025-01-01
abbr: "S-CDR"
fullName: "SGSN (IP-CAN bearer) generated – Charging Data Record"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/s-cdr/"
summary: "Specifický typ záznamu účtovacích dat (Charging Data Record) generovaný SGSN pro služby paketové (PS) domény. Podrobně popisuje využití prostředků pro přenosový kanál IP-CAN (IP Connectivity Access Ne"
---

S-CDR je záznam účtovacích dat (Charging Data Record) generovaný SGSN pro paketově spínané služby, který podrobně popisuje využití prostředků přenosového kanálu IP-CAN, jako je objem dat a doba trvání, pro offline účtování a fakturaci.

## Popis

S-CDR ([SGSN](/mobilnisite/slovnik/sgsn/) generovaný [CDR](/mobilnisite/slovnik/cdr/) pro přenosový kanál [IP-CAN](/mobilnisite/slovnik/ip-can/)) je standardizovaný záznam dat definovaný 3GPP pro offline účtování v paketově spínané jádrové síti. Generuje ho Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) během datové relace uživatele. S-CDR konkrétně eviduje využití přenosového kanálu IP Connectivity Access Network (IP-CAN), což je logický kanál poskytující IP konektivitu mezi uživatelským zařízením (UE) a paketovou datovou sítí ([PDN](/mobilnisite/slovnik/pdn/)). Vytvoření a uzavření S-CDR je spouštěno specifickými událostmi v životním cyklu přenosového kanálu, jako je jeho zřízení, změna (např. QoS) a ukončení. Během relace SGSN shromažďuje účtovací informace v reálném čase, které jsou následně formátovány do CDR a přeneseny přes rozhraní Ga do funkce Charging Gateway Function ([CGF](/mobilnisite/slovnik/cgf/)).

Struktura S-CDR je velmi podrobná a skládá se z mnoha polí podle 3GPP TS 32.251 a TS 32.298. Mezi klíčová datová pole patří Record Sequence Number pro řazení, [IMSI](/mobilnisite/slovnik/imsi/) a [IMEI](/mobilnisite/slovnik/imei/) pro identifikaci účastníka a zařízení, adresy SGSN, použitý Access Point Name (APN) a identifikátory PDP kontextu. Zásadně obsahuje metriky využití: přenesený objem dat (odděleně pro uplink a downlink), dobu trvání relace a parametry QoS (jako QoS Class Identifier - QCI, Allocation and Retention Priority - ARP a zaručená/maximální přenosová rychlost), které byly aktivní během životnosti přenosového kanálu. Záznam také časově označuje všechny významné události a může obsahovat informace o poloze (jako Routing Area a Cell Global Identity) a kódy příčin ukončení relace.

V širší účtovací architektuře S-CDR funguje ve spojení s dalšími typy CDR. Pro typickou datovou relaci jsou generovány S-CDR ze SGSN a G-CDR z GGSN/PGW. S-CDR se zaměřuje na přístupovou síť a využití rádiových prostředků spravovaných SGSN, zatímco G-CDR se zaměřuje na konektivitu externí datové sítě a objem dat. Funkce Charging Data Function (CDF) uvnitř SGSN tyto záznamy sestavuje. Jsou poté odeslány přes Charging Gateway Function (CGF) do Billing Domain (BD) pro mediaci, ocenění a nakonec generování faktur. S-CDR je tedy atomickou jednotkou fakturačních informací, poskytující podrobný detail nezbytný pro složité tarifní modely, jako jsou stupňovité datové tarify, účtování podle denní doby nebo fakturace rozlišená podle QoS.

## K čemu slouží

S-CDR byl vytvořen pro umožnění přesného a standardizovaného offline (post-paid) účtování pro paketově spínané služby mobilních dat v sítích 2.5G (GPRS) a 3G (UMTS). Před jeho standardizací bylo fakturace datových služeb roztříštěná a proprietární. S-CDR řeší kritický obchodní problém měření a zaznamenávání spotřeby prostředků v paketovém jádru způsobem, který umožňuje interoperabilitu mezi dodavateli. Poskytuje operátorům spolehlivou auditní stopu pro využití, ke kterému dochází v působnosti SGSN, který spravuje mobilitu a řízení relací v přístupové síti.

Jeho zavedení v 3GPP Release 6 bylo součástí širšího úsilí o dozrání účtovacího rámce paketového jádra, v souladu s růstem mobilních dat přesahujícím jednoduché WAP prohlížení. S-CDR řeší potřebu účtovat nejen za surový objem dat, ale také za poskytovanou kvalitu služby. Zahrnutím detailních parametrů QoS umožňuje nové obchodní modely, kde prémiové služby (jako streamování videa) mohou být účtovány odlišně od běžného webového prohlížení. Navíc jeho oddělení od G-CDR umožňuje podrobnější izolaci chyb a alokaci nákladů mezi funkce rádiového přístupu/jádrové sítě a bránové funkce připojující se k internetu. Toto podrobné účtování bylo zásadní pro komerční zavedení paušálních a balíčkových datových tarifů, protože dalo operátorům nástroje k pochopení vzorců využití sítě a nákladových struktur.

## Klíčové vlastnosti

- Generován SGSN pro relaci přenosového kanálu IP-CAN
- Zaznamenává spotřebu objemu dat (uplink/downlink odděleně)
- Zachycuje dobu trvání relace s přesnými časovými razítky
- Zahrnuje parametry QoS (QCI, ARP, přenosové rychlosti) pro diferenciaci služeb
- Obsahuje identifikátory účastníka (IMSI, MSISDN) a informace o APN
- Přenášen přes rozhraní Ga do Charging Gateway pro zpracování fakturace

## Související pojmy

- [G-CDR – GGSN (PDP context) generated - Charging Data Record](/mobilnisite/slovnik/g-cdr/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [IP-CAN – IP-Connectivity Access Network](/mobilnisite/slovnik/ip-can/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)

## Definující specifikace

- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification

---

📖 **Anglický originál a plná specifikace:** [S-CDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-cdr/)
