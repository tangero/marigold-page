---
slug: "dck"
url: "/mobilnisite/slovnik/dck/"
type: "slovnik"
title: "DCK – Depersonalisation Control Keys"
date: 2025-01-01
abbr: "DCK"
fullName: "Depersonalisation Control Keys"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dck/"
summary: "DCK (Depersonalisation Control Keys) jsou kryptografické klíče používané v sítích 3GPP k bezpečnému vymazání nebo resetu personalizačních dat na univerzálních integrovaných obvodech (UICC). Umožňují a"
---

DCK je kryptografický klíč používaný v sítích 3GPP k bezpečnému vymazání personalizačních dat na UICC, což umožňuje autorizovanou vzdálenou depersonalizaci SIM karet pro účely zabezpečení a správy zařízení.

## Popis

Depersonalisation Control Keys (DCK) jsou základním bezpečnostním mechanismem definovaným ve specifikacích 3GPP pro správu životního cyklu aplikací na UICC (Universal Integrated Circuit Card), konkrétně modulu SIM a USIM. Tyto klíče jsou součástí protokolů zabezpečeného kanálu navázaného mezi systémy síťového operátora a UICC. DCK slouží k autorizaci a provedení příkazu depersonalizace, který bezpečně vymaže personalizovaná data, jako je International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), autentizační klíče (Ki) a další konfigurace specifické pro operátora, z karty. Tento proces učiní UICC nepoužitelnou v síti a vrátí ji do prázdného nebo továrního stavu, čímž zabrání jejímu neoprávněnému opětovnému použití.

Architektura pro fungování DCK zahrnuje několik klíčových komponent: UICC obsahující zabezpečený souborový systém a aplikace, mobilní zařízení ([ME](/mobilnisite/slovnik/me/)), které poskytuje fyzické rozhraní, a Over-The-Air ([OTA](/mobilnisite/slovnik/ota/)) platformu nebo provizní systém operátora. Samotný DCK je symetrický kryptografický klíč, typicky 128bitový, který je bezpečně uložen jak v zabezpečeném systému pro správu klíčů operátora, tak v chráněné oblasti UICC během fáze personalizace. Když je vyžadována depersonalizace, síťový operátor zahájí zabezpečenou relaci pomocí DCK k ověření příkazu. UICC ověří pravost příkazu pomocí uloženého DCK před provedením nevratného smazání personalizovaných dat.

Technicky proces depersonalizace následuje specifikaci 3GPP TS 31.102 pro aplikace USIM. DCK je používán v rámci zabezpečené obálky zprávy, často za použití Secure Channel Protocol (SCP) s kryptografickými mechanismy jako [AES](/mobilnisite/slovnik/aes/) nebo [DES](/mobilnisite/slovnik/des/). Struktura příkazu zahrnuje autentizační kódy ([MAC](/mobilnisite/slovnik/mac/)) vypočítané pomocí DCK pro zajištění integrity a pravosti. Úspěšné provedení zahrnuje vymazání citlivých souborů ze struktury Elementary Files ([EF](/mobilnisite/slovnik/ef/)) na UICC, zejména těch v adresářích [DF](/mobilnisite/slovnik/df/)_GSM a DF_5GS, a případné uzamčení karty pro další použití. Tento mechanismus se liší od PIN unblocking keys (PUK) nebo administrátorských kódů, protože cílí na úplné odstranění síťových přihlašovacích údajů, nikoli pouze na odemčení přístupu.

Role DCK v síťovém ekosystému je mnohostranná. Slouží jako klíčový nástroj pro operátory ke správě bezpečnostních incidentů, například když je UICC nahlášena jako odcizená nebo kompromitovaná. Použitím DCK mohou operátory vzdáleně deaktivovat kartu a zabránit tak podvodům. Také usnadňuje efektivní recyklaci a opětovné provizování UICC v rámci správy zásob. Dále mechanismy DCK podporují regulatorní požadavky na ochranu osobních údajů tím, že zajišťují bezpečné vymazání osobních dat při ukončení služby účastníkem. Zabezpečené zacházení a uložení DCK v infrastrukturách operátorů podléhá přísným bezpečnostním politikám, protože kompromitace těchto klíčů by mohla umožnit neoprávněnou depersonalizaci nebo jiné škodlivé akce proti kartám účastníků.

## K čemu slouží

DCK byl zaveden, aby řešil rostoucí potřebu bezpečné vzdálené správy UICC karet v mobilních sítích. Před standardizovanými mechanismy depersonalizace čelili operátoři značným výzvám při řešení ztracených, odcizených nebo kompromitovaných SIM karet. Bez možnosti bezpečného vzdáleného vymazání mohly být tyto karty nadále zneužívány k podvodům, což vedlo ke ztrátám příjmů a bezpečnostním narušením. Manuální procesy pro zařazení IMSI na černou listinu byly reaktivní a pomalé a neodstraňovaly přihlašovací údaje z fyzické karty samotné, což ponechávalo prostor pro zneužití v jiných sítích nebo na klonovaných zařízeních.

Vytvoření DCK bylo motivováno vývojem směrem k Over-The-Air (OTA) správě UICC, která umožnila operátorům provizovat, aktualizovat a spravovat karty bez fyzického přístupu. Jak se sítě rozšiřovaly a základna účastníků rostla do milionů, schopnost efektivně a bezpečně spravovat ukončení životnosti karet nebo nápravu bezpečnostních incidentů se stala nezbytnou. DCK poskytl standardizovanou, kryptograficky zabezpečenou metodu pro autorizaci příkazů depersonalizace, což zajišťuje, že tuto kritickou funkci mohou provádět pouze autorizovaní síťoví operátoři. Tím byly řešeny limity proprietárních řešení a byla posílena interoperabilita mezi různými výrobci UICC a systémy operátorů.

Historicky zavedení DCK v Release 6 korespondovalo s širším úsilím 3GPP o vylepšené bezpečnostní funkce pro sítě 3G/UMTS. Doplnilo další bezpečnostní mechanismy, jako je protokol Authentication and Key Agreement (AKA) a zabezpečené OTA platformy. Tím, že poskytl řízenou metodu pro vymazání personalizovaných dat, pomohl DCK udržet integritu systému identit účastníků, chránit před útoky klonování SIM karet a podporovat soulad s předpisy o ochraně dat, které nařizují bezpečné vymazání osobních informací při ukončení služby.

## Klíčové vlastnosti

- Kryptografická autentizace příkazů depersonalizace
- Bezpečné vymazání IMSI a autentizačního klíče (Ki) z UICC
- Integrace s OTA platformou pro vzdálenou správu
- Ochrana proti neoprávněnému opětovnému použití karet a podvodům
- Soulad s regulacemi ochrany osobních údajů pro mazání přihlašovacích údajů
- Standardizovaná struktura příkazu dle 3GPP TS 31.102

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification

---

📖 **Anglický originál a plná specifikace:** [DCK na 3GPP Explorer](https://3gpp-explorer.com/glossary/dck/)
