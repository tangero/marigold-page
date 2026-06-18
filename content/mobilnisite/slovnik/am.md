---
slug: "am"
url: "/mobilnisite/slovnik/am/"
type: "slovnik"
title: "AM – Access and Mobility Management"
date: 2025-01-01
abbr: "AM"
fullName: "Access and Mobility Management"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/am/"
summary: "AM je funkce jádra sítě zodpovědná za správu přístupu uživatelského zařízení k síti a za řízení mobilních procedur. Autentizuje uživatele, autorizuje přístup k síti a spravuje sledování polohy a předá"
---

AM je funkce jádra sítě zodpovědná za správu přístupu uživatelského zařízení, autentizaci uživatelů, autorizaci přístupu k síti a za řízení mobilních procedur, jako je sledování polohy a předávání hovoru (handover).

## Popis

Správa přístupu a mobility (AM) je základní funkční entita v síťové architektuře 3GPP, konkrétně součást funkce [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function) v systémech 5G. Slouží jako primární koncový bod pro signalizaci Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) od uživatelského zařízení (UE) a zajišťuje všechny procedury související s počáteční registrací, správou připojení a mobilitou. Funkce AM je zodpovědná za vytvoření a udržování registračního stavu UE v síti, což je základ pro všechny následné komunikační služby.

Architektonicky AM funguje v řídicí rovině jádra sítě a komunikuje s ostatními síťovými funkcemi prostřednictvím rozhraní založených na službách. V 5G AMF (který hostí funkcionalitu AM) komunikuje s funkcí [SMF](/mobilnisite/slovnik/smf/) (Session Management Function) při zakládání [PDU](/mobilnisite/slovnik/pdu/) sezení, s funkcí [AUSF](/mobilnisite/slovnik/ausf/) (Authentication Server Function) pro bezpečnostní procedury a s [UDM](/mobilnisite/slovnik/udm/) (Unified Data Management) pro data účastníka. Také se připojuje k rádiové přístupové síti (RAN) přes rozhraní [N2](/mobilnisite/slovnik/n2/), přijímá počáteční přístupové požadavky a spravuje signalizaci předávání hovoru. Funkce AM udržuje kontext UE, který zahrnuje registrační stav UE, bezpečnostní kontext, informace o poloze a předplatitelská data.

Fungování AM zahrnuje několik klíčových procedur. Při počátečním přístupu odešle UE prostřednictvím RAN požadavek na registraci do AMF. Funkce AM autentizuje UE pomocí přihlašovacích údajů uložených v UDM a vytvoří bezpečnostní kontext. Následně autorizuje přístup UE na základě profilů předplatného a síťových politik. Pro správu mobility AM sleduje polohu UE s přesností na úroveň registrační oblasti (skupiny sledovacích oblastí) a spravuje procedury jako aktualizace registrační oblasti a předávání hovoru mezi různými oblastmi obsluhovanými AMF. Funkce AM také zajišťuje správu připojení, přechody UE mezi stavy CM-IDLE a CM-CONNECTED, což řídí, zda má UE signalizační spojení s AMF.

Role AM v síti je kritická z několika důvodů. Za prvé zajišťuje, že k síťovým prostředkům mají přístup pouze autorizovaná zařízení, což představuje první linii zabezpečení. Za druhé umožňuje plynulou mobilitu prostřednictvím správy sledování polohy a předávání hovoru bez přerušení aktivních sezení. Za třetí optimalizuje využití síťových prostředků řízením okamžiku, kdy UE navazují signalizační spojení. Nakonec AM poskytuje základ pro ostatní síťové služby tím, že udržuje registrační stav a kontext UE, což je nezbytné pro správu sezení, uplatňování politik a účtování.

## K čemu slouží

Funkce správy přístupu a mobility (AM) existuje proto, aby poskytla centralizovaný a efektivní mechanismus pro řízení způsobu, jakým se uživatelská zařízení připojují k mobilním sítím a pohybují se jimi. Před formalizací AM ve standardech 3GPP byly řízení přístupu a správa mobility často řešeny proprietárními nebo méně integrovanými řešeními, která vedla k problémům s interoperabilitou, neefektivním předáváním hovoru a bezpečnostním slabinám. Vytvoření AM odpovědělo na potřebu standardizovaného přístupu, který by dokázal škálovat s rostoucím počtem účastníků a podporovat stále složitější scénáře mobility.

Historicky, jak se mobilní sítě vyvíjely od 2G přes 3G a dále, se výzvy spojené se správou mobility uživatelů stávaly výraznějšími. Rané systémy měly omezené možnosti předávání hovoru a základní autentizační mechanismy. Zavedení AM v 3GPP Release 4 poskytlo komplexní rámec, který oddělil správu přístupu a mobility od správy sezení, což umožnilo flexibilnější síťové architektury. Toto oddělení se stalo obzvláště důležitým při přechodu na plně IP sítě a potřebě podporovat více přístupových technologií (jako 2G, 3G, LTE a ne-3GPP přístup).

Funkce AM řeší několik klíčových problémů: poskytuje jednotný bod řízení pro registraci a autentizaci UE napříč různými typy přístupu; umožňuje efektivní sledování polohy UE bez nadměrné signalizační režie; podporuje plynulou mobilitu mezi buňkami a mezi různými rádiovými přístupovými technologiemi; a poskytuje bezpečnostní základ pro všechny následné síťové interakce. Řešením těchto problémů AM umožňuje spolehlivý, bezpečný a efektivní provoz moderních mobilních sítí, které podporují miliardy připojených zařízení s různými vzorci mobility.

## Klíčové vlastnosti

- Procedury registrace a deregistrace UE
- Autentizace a autorizace přístupu k síti
- Správa připojení (stavy CM-IDLE/CM-CONNECTED)
- Správa registrační oblasti a aktualizace sledovacích oblastí
- Signalizace předávání hovoru a mobilita mezi AMF
- Ukončení NAS signalizace a zabezpečení

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.815** (Rel-14) — Study on Multimedia Broadcast Supplement for PWS
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TS 29.519** (Rel-19) — UDR Usage for Policy & Exposure Data
- **TS 29.521** (Rel-19) — 5G Binding Support Management Service Stage 3
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 32.859** (Rel-12) — Alarm Management Quality Improvement Study
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [AM na 3GPP Explorer](https://3gpp-explorer.com/glossary/am/)
