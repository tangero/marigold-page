---
slug: "pck-id"
url: "/mobilnisite/slovnik/pck-id/"
type: "slovnik"
title: "PCK-ID – Private Call Key Identifier"
date: 2026-01-01
abbr: "PCK-ID"
fullName: "Private Call Key Identifier"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pck-id/"
summary: "Identifikátor kryptografického klíče používaného k zabezpečení komunikace v privátních skupinách ve službách Mission Critical Push-to-Talk (MCPTT). Umožňuje bezpečnou distribuci a správu klíčů pro šif"
---

PCK-ID je identifikátor kryptografického klíče používaného k zabezpečení komunikace v privátních skupinách ve službách Mission Critical Push-to-Talk (MCPTT).

## Popis

Private Call Key Identifier (PCK-ID) je klíčový bezpečnostní parametr v architektuře 3GPP Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), konkrétně pro službu Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Funguje jako jedinečný štítek nebo odkaz na konkrétní Private Call Key ([PCK](/mobilnisite/slovnik/pck/)), což je symetrický kryptografický klíč. Tento klíč se používá k ochraně privátních skupinových hovorů, což je základní funkce MCPTT umožňující předem definované, uzavřené skupině uživatelů bezpečně komunikovat. PCK-ID není samotný klíč, ale ukazatel (handle), který síť a uživatelské zařízení (UE) používají k identifikaci, který klíč má být použit pro konkrétní relaci privátní skupiny.

Architektura zahrnuje několik funkčních entit definovaných v 3GPP TS 23.280. Key Management Server ([KMS](/mobilnisite/slovnik/kms/)) je zodpovědný za generování, distribuci a správu životního cyklu Private Call Keys. Když je založena privátní skupina nebo je její klíč aktualizován, KMS vygeneruje nový PCK a přiřadí mu jedinečný PCK-ID. Tento PCK a jeho přidružený PCK-ID jsou následně bezpečně zřízeny do UE členů skupiny prostřednictvím MCPTT serveru. Zřizování obvykle probíhá přes zabezpečené signalizační kanály, často s využitím procedur autorizace služby MCPTT a navázání klíče.

Během sestavování privátního skupinového hovoru volající MCPTT klient zahrne příslušný PCK-ID do signalizace zahájení relace (např. v rámci [SIP](/mobilnisite/slovnik/sip/)/[SDP](/mobilnisite/slovnik/sdp/) nebo specifických zpráv protokolu MCPTT). Po přijetí volaná UE použijí PCK-ID k nalezení odpovídajícího PCK bezpečně uloženého v jejich lokálním úložišti klíčů. Jakmile je správný klíč identifikován, je použit pro šifrování médií (např. pomocí [AES](/mobilnisite/slovnik/aes/)) a autentizaci zpráv po dobu trvání hovoru. Tento proces zajišťuje, že pouze UE vlastnící klíč odkazovaný PCK-ID mohou dešifrovat média a ověřit pravost přenosu, čímž se vynucuje důvěrnost a integrita skupiny.

Role PCK-ID přesahuje pouhé sestavení hovoru. Je nedílnou součástí operací správy klíčů, jako je obnova, odvolání a synchronizace klíčů. Pokud je klíč kompromitován nebo člen skupinu opustí, KMS může vygenerovat nový PCK, přiřadit nový PCK-ID a distribuovat jej zbývajícím autorizovaným členům, čímž efektivně provede změnu klíče skupiny. PCK-ID umožňuje systému jasně rozlišit mezi starým a novým klíčem, což zajišťuje plynulý přechod bez přerušení služby. Jeho specifikace napříč více technickými specifikacemi (TS), včetně těch pro bezpečnost (33-series) a protokolové detaily (24-series a 29-series), podtrhuje jeho zásadní roli v komplexním bezpečnostním modelu pro skupinovou komunikaci v misi-kritických službách.

## K čemu slouží

PCK-ID byl zaveden, aby řešil přísné bezpečnostní požadavky profesionální a misi-kritické komunikace, jako je ta používaná složkami integrovaného záchranného systému, pohotovostními službami a organizacemi z oblasti energetiky. Tradiční komerční služby skupinové komunikace postrádaly robustní, řízené kryptografické zabezpečení potřebné pro citlivé operace, kde by odposlech nebo zneužití identity mohly mít závažné následky. Hlavní problém, který PCK-ID řeší, je bezpečné a efektivní propojení kryptografických klíčů s konkrétními privátními komunikačními skupinami v rámci škálovatelného, standardizovaného rámce.

Historicky bezpečná skupinová hlasová komunikace často spoléhala na proprietární systémy nebo méně dynamickou správu klíčů, což ztěžovalo interoperabilitu a znesnadňovalo aktualizace klíčů. Standardizace Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)) ze strany 3GPP si kladla za cíl vytvořit globální standard založený na LTE/5G. Základním požadavkem bylo umožnění bezpečných privátních skupinových hovorů. Koncept PCK-ID poskytuje potřebnou abstrakci, která umožňuje infrastruktuře správy klíčů aktualizovat kryptografický materiál bez změny logické identity skupiny a umožňuje UE jednoznačně vybrat správný klíč z potenciálně několika uložených klíčů pro různé skupiny.

Jeho vytvoření bylo motivováno potřebou standardizovaného identifikátoru, který funguje v souladu s bezpečnostní architekturou 3GPP pro MCPTT, definovanou v TS 33.179 a TS 33.180. Řeší problém identifikace klíče a správy jeho životního cyklu v síti, kde uživatelé mohou současně patřit do více privátních skupin. Použitím PCK-ID systém zajišťuje, že pro šifrování a ochranu integrity každého privátního hovoru je použit správný klíč, čímž udržuje důvěrnost a brání neoprávněnému přístupu, což je prvořadé pro komunikaci, na níž závisí životy.

## Klíčové vlastnosti

- Jedinečný identifikátor pro symetrický Private Call Key (PCK) používaný v MCPTT.
- Umožňuje bezpečné propojení mezi kryptografickým klíčem a konkrétní relací privátního skupinového hovoru.
- Usnadňuje distribuci klíčů a správu jejich životního cyklu (např. obnovu, odvolání) prostřednictvím Key Management Server (KMS).
- Používá se v hovorové signalizaci (např. SIP/SDP) k označení, který klíč mají účastníci použít.
- Umožňuje uživatelskému zařízení (UE) vybrat správný klíč z lokálního zabezpečeného úložiště pro šifrování/dešifrování médií.
- Nezbytný pro udržení důvěrnosti a integrity misi-kritické komunikace v privátních skupinách.

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.879** (Rel-13) — MCPTT Security Study

---

📖 **Anglický originál a plná specifikace:** [PCK-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/pck-id/)
