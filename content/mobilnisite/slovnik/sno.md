---
slug: "sno"
url: "/mobilnisite/slovnik/sno/"
type: "slovnik"
title: "SNO – Secondary Network Operator"
date: 2025-01-01
abbr: "SNO"
fullName: "Secondary Network Operator"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sno/"
summary: "Obchodní role ve scénářích sdílení sítě, kde operátor nevlastní rádiové spektrum ani primární síťovou infrastrukturu, ale poskytuje komerční služby pronájmem kapacity od primárního operátora (MNO). Um"
---

SNO (sekundární síťový operátor) je sekundární síťový operátor, který poskytuje komerční mobilní služby pronájmem kapacity rádiového přístupu od primárního MNO, což umožňuje vstup na trh bez vlastnictví spektra nebo hlavní infrastruktury.

## Popis

Sekundární síťový operátor (SNO) je obchodní a provozní entita definovaná v rámci architektury sdílení sítí 3GPP. SNO nevlastní licenci na rádiové spektrum ani primární infrastrukturu rádiové přístupové sítě (RAN). Místo toho funguje jako entita podobná mobilnímu virtuálnímu síťovému operátorovi ([MVNO](/mobilnisite/slovnik/mvno/)), která uzavře obchodní dohodu s primárním síťovým operátorem ([PNO](/mobilnisite/slovnik/pno/)), též známým jako mobilní síťový operátor ([MNO](/mobilnisite/slovnik/mno/)), aby využívala sdílené síťové zdroje PNO k poskytování vlastních služeb koncovým uživatelům.

Z architektonického hlediska sdílení sítě umožňuje více operátorům jádrové sítě (každý se svými vlastními uzly jádrové sítě, jako je [MME](/mobilnisite/slovnik/mme/), [SGW](/mobilnisite/slovnik/sgw/), [PGW](/mobilnisite/slovnik/pgw/) v 4G, nebo [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), UPF v 5G) připojit se ke sdílené rádiové přístupové síti. SNO vlastní své vlastní jádro sítě, databáze účastníků (HSS/UDM) a případně vlastní servisní platformy. Z pohledu sdílené RAN je provoz z uživatelských zařízení (UE) různých operátorů rozlišován pomocí specifických síťových identifikátorů, především PLMN ID. Sdílená RAN (např. eNB/gNB) je nakonfigurována k vysílání PLMN ID jak PNO, tak SNO a směruje uživatelská data a signalizaci do příslušné jádrové sítě na základě vybraného PLMN.

Princip fungování: Účastník s předplatným od SNO má SIM/USIM kartu naprogramovanou s PLMN ID SNO. Když se UE připojí ke sdílené buňce, vidí v broadcast systémové informaci obě PLMN ID. Vybere si PLMN své domovské SNO. RAN při navázání spojení použije toto vybrané PLMN ID k nasměrování úvodní signalizační zprávy (např. Attach Request, Registration Request) k prvku jádrové sítě (např. MME, AMF) patřícímu k tomuto konkrétnímu PLMN/operátorovi. To umožňuje SNO mít plnou kontrolu nad autentizací svých účastníků, správou relací a politikami, přičemž je závislé na PNO pro rádiové pokrytí a kapacitu.

## K čemu slouží

Koncept sekundárního síťového operátora byl standardizován, aby usnadnil flexibilnější a efektivnější tržní struktury v telekomunikačním průmyslu. Řeší vysokou vstupní bariéru způsobenou obrovskými kapitálovými výdaji (CAPEX) potřebnými k získání licencí na spektrum a vybudování celostátní rádiové sítě. Model SNO umožňuje novým poskytovatelům služeb rychlý vstup na trh pronájmem síťové kapacity, čímž podporuje konkurenci a inovace.

Jeho zavedení bylo motivováno regulatorní snahou o zvýšení konkurence a efektivnější využití vzácného rádiového spektra a fyzické infrastruktury (jako jsou lokalit BTS). Řeší problém duplikace infrastruktury, umožňuje existenci více poskytovatelů služeb, aniž by každý z nich musel budovat překrývající se rádiové sítě. To je zvláště cenné ve scénářích, jako je pokrytí venkovských oblastí, kde může být jediná vybudovaná infrastruktura sdílena, nebo pro niky zaměřené operátory cílicí na specifické skupiny zákazníků bez břemene vlastnictví RAN. Specifikace 3GPP poskytují technické prostředky (jako je sdílení RAN s více PLMN), které činí takové obchodní modely provozně proveditelnými.

## Klíčové vlastnosti

- Funguje bez vlastnictví licencovaného rádiového spektra nebo infrastruktury RAN
- Vlastní vlastní uzly jádrové sítě a systémy správy účastníků
- Používá unikátní PLMN ID k identifikaci své sítě vůči uživatelskému zařízení
- Spoléhá se na obchodní dohodu s primárním síťovým operátorem (PNO/MNO) pro přístup k RAN
- Rozšiřuje tržní konkurenci a umožňuje vstup nových subjektů zaměřených na služby
- Podporován architekturami pro sdílení sítí 3GPP, jako je MORAN (Multi-Operator RAN) a MOCN (Multi-Operator Core Network)

## Související pojmy

- [MNO – Mobile Network Operator](/mobilnisite/slovnik/mno/)
- [MVNO – Mobile Virtual Network Operator](/mobilnisite/slovnik/mvno/)
- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)

## Definující specifikace

- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TR 22.912** (Rel-19) — Network Selection for Non-3GPP Access
- **TR 22.937** (Rel-13) — FMC requirements for 3GPP-WLAN service continuity

---

📖 **Anglický originál a plná specifikace:** [SNO na 3GPP Explorer](https://3gpp-explorer.com/glossary/sno/)
