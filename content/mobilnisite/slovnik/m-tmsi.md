---
slug: "m-tmsi"
url: "/mobilnisite/slovnik/m-tmsi/"
type: "slovnik"
title: "M-TMSI – M-Temporary Mobile Subscriber Identity"
date: 2025-01-01
abbr: "M-TMSI"
fullName: "M-Temporary Mobile Subscriber Identity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/m-tmsi/"
summary: "Dočasný identifikátor účastníka používaný v procedurách správy mobility (EMM) mezi UE a MME. Zajišťuje soukromí identity uživatele na rádiovém rozhraní tím, že skrývá trvalý IMSI, a používá se pro vol"
---

M-TMSI je dočasný identifikátor účastníka používaný v rámci správy mobility v EPS (Evolved Packet System) k zajištění soukromí identity uživatele tím, že na rádiovém rozhraní skrývá trvalý IMSI.

## Popis

M-Temporary Mobile Subscriber Identity (M-TMSI) je identifikátor používaný v jádře sítě v rámci Evolved Packet System (EPS) pro správu mobility. Přiřazuje jej Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) uživatelskému zařízení (UE) během procedury připojení (attach) nebo následné aktualizace sledované oblasti (tracking area update). Primární funkcí M-TMSI je sloužit jako dočasný alias pro trvalý, na předplatném založený International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), čímž zvyšuje soukromí účastníka na rádiovém rozhraní. Z architektonického hlediska je M-TMSI 32bitová hodnota používaná v rámci Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) protokolu, který si přímo vyměňují UE a MME. Jeho fungování je nedílnou součástí procesů připojení k EPS a volání (paging). Při počátečním připojení k síti, pokud UE poskytne svůj IMSI, MME účastníka autentizuje a může mu přidělit nové M-TMSI. Toto M-TMSI je poté zašifrované v NAS signalizaci odesláno UE. Pro následnou komunikaci, jako je servisní požadavek nebo odpověď na volací zprávu (paging), UE v NAS zprávě použije M-TMSI místo IMSI. Když MME potřebuje zavolat UE (např. pro příchozí hovor), použije k sestavení identifikátoru pro volání právě M-TMSI. [S-TMSI](/mobilnisite/slovnik/s-tmsi/), což je pro účely rádiové efektivity zkrácená verze, je ve skutečnosti konkatenací kódu MME ([MMEC](/mobilnisite/slovnik/mmec/)) a M-TMSI. MME ve své databázi udržuje mapování mezi přiděleným M-TMSI a IMSI účastníka a dalšími kontextovými údaji. Jeho role je klíčová pro snížení signalizační režie (je kratší než IMSI) a pro implementaci důvěrnosti identity, protože citlivý IMSI je po počáteční registraci zřídkakdy přenášen v nezašifrované podobě. M-TMSI je platný v oblasti přidělujícího MME; pokud se UE přesune do oblasti obsluhované jiným MME, může být přiděleno nové M-TMSI.

## K čemu slouží

M-TMSI bylo vytvořeno, aby řešilo dva klíčové problémy v mobilních sítích: soukromí identity účastníka a efektivitu signalizace. Trvalý [IMSI](/mobilnisite/slovnik/imsi/), pokud by byl často přenášen v nezašifrované podobě, by mohl být použit ke sledování polohy a aktivit uživatele. Účelem M-TMSI je po počáteční autentizaci zastřít tuto trvalou identitu na rádiovém rozhraní. Řeší problém soukromí tím, že pro většinu transakcí [NAS](/mobilnisite/slovnik/nas/) signalizace poskytuje dočasný, často se měnící identifikátor. Dále je 32bitové M-TMSI (a jeho odvozená forma [S-TMSI](/mobilnisite/slovnik/s-tmsi/)) kratší než až 15místný IMSI, což vede k efektivnějšímu využití rádiových zdrojů ve volacích zprávách (paging) a signalizačních procedurách. Historicky existovaly dočasné identifikátory jako TMSI již v GSM a UMTS. M-TMSI je ekvivalentní identifikátor pro EPS, přizpůsobený plně IP a plošší architektuře LTE/EPC. Jeho zavedení ve verzi 8 (Release 8) bylo motivováno potřebou zachovat a posílit ochranu soukromí účastníků v nové architektuře 4G systému a zároveň optimalizovat signalizační zátěž pro obrovské množství připojených zařízení. Umožňuje síti jednoznačně identifikovat UE pro účely správy mobility, aniž by byly neustále vystavovány trvalé přihlašovací údaje účastníka.

## Klíčové vlastnosti

- 32bitový dočasný identifikátor přidělovaný MME uživatelskému zařízení (UE)
- Používá se k zachování soukromí identity účastníka skrytím IMSI
- Využívá se v signalizaci na vrstvě NAS mezi UE a MME (např. Servisní požadavek, Odpověď na volání)
- Je součástí S-TMSI (MMEC + M-TMSI) používaného pro efektivní rádiové volání (paging)
- Platný v rámci oblasti přidělujícího MME
- Měněn periodicky nebo při specifických událostech (např. předávání mezi MME) pro zvýšení bezpečnosti

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [S-TMSI – SAE Temporary Mobile Subscriber Identity](/mobilnisite/slovnik/s-tmsi/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [GUTI – Globally Unique Temporary UE Identity](/mobilnisite/slovnik/guti/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC

---

📖 **Anglický originál a plná specifikace:** [M-TMSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/m-tmsi/)
