---
slug: "spk-id"
url: "/mobilnisite/slovnik/spk-id/"
type: "slovnik"
title: "SPK-ID – Signalling Protection Key Identifier"
date: 2025-01-01
abbr: "SPK-ID"
fullName: "Signalling Protection Key Identifier"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/spk-id/"
summary: "Jedinečný identifikátor klíče pro zabezpečení signalizace používaný k ochraně komunikace mezi UE a síťovou funkcí. Je klíčový pro zajištění ochrany integrity a důvěrnosti signalizačních zpráv, zejména"
---

SPK-ID je jedinečný identifikátor klíče pro zabezpečení signalizace, který chrání komunikaci mezi uživatelským zařízením a síťovou funkcí a umožňuje integritu a důvěrnost signalizačních zpráv.

## Popis

Identifikátor klíče pro zabezpečení signalizace (SPK-ID) je bezpečnostní parametr definovaný v architektuře 3GPP, konkrétně pro protokoly jako NASCON ([NAS](/mobilnisite/slovnik/nas/) Security Context) a procedury zahrnující IP Multimedia Core Network Subsystem (IMS). Není to samotný klíč, ale odkaz nebo štítek, který odkazuje na konkrétní kryptografický klíčový kontext vytvořený mezi uživatelským zařízením (UE) a síťovou entitou, jako je funkce pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5G nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G. Tento klíčový kontext se používá k aplikaci ochrany integrity a volitelně šifrování na signalizační zprávy Non-Access Stratum (NAS) nebo jinou citlivou komunikaci řídicí roviny. SPK-ID umožňuje síti a UE jednoznačně identifikovat, která sada bezpečnostních klíčů a algoritmů má být použita pro konkrétní signalizační relaci nebo proceduru, což umožňuje efektivní správu klíčů a přepínání kontextů.

Architektura zahrnující SPK-ID je integrována do bezpečnostních procedur jádra sítě. Když je vytvořen bezpečnostní kontext – například během procedury Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) – síť přiřadí SPK-ID spolu s odvozenými klíči (jako je klíč integrity ([IK](/mobilnisite/slovnik/ik/)) a šifrovací klíč ([CK](/mobilnisite/slovnik/ck/))). Tento identifikátor je pak uložen v bezpečnostním kontextu UE a v odpovídající síťové funkci. Během následných signalizačních výměn může být SPK-ID zahrnuto v hlavičkách zpráv nebo implicitně odkazováno, což umožňuje oběma stranám rychle získat správný kryptografický materiál bez opětovného vyjednávání bezpečnostních parametrů. Tento mechanismus je zásadní pro služby vyžadující trvalé, zabezpečené relace, jako je registrace v IMS a nastavení hovoru, kde je integrita signalizace prvořadá pro prevenci podvržení a útoků typu man-in-the-middle.

Klíčovými komponentami v ekosystému SPK-ID jsou univerzální [SIM](/mobilnisite/slovnik/sim/) karta ([USIM](/mobilnisite/slovnik/usim/)) v UE, která se účastní AKA k vygenerování kořenových klíčů, a funkce jádra sítě jako Security Anchor Function (SEAF) a Authentication Server Function (AUSF) v 5G nebo Home Subscriber Server (HSS) v 4G/IMS. Úlohou SPK-ID je fungovat jako lehký index v rámci širší hierarchie klíčů, která zahrnuje K_{ASME} v EPS nebo K_{SEAF} v 5G. Použitím identifikátoru se systém vyhne přenosu plných klíčů vzduchem a podporuje více souběžných bezpečnostních kontextů pro různé služby na stejném UE. Jeho specifikace napříč dokumenty jako TS 24.380 (IMS) a TS 29.380 (systém 5G) zajišťuje interoperabilitu mezi implementacemi UE a sítě od různých dodavatelů.

## K čemu slouží

SPK-ID byl zaveden, aby řešil rostoucí potřebu robustního a spravovatelného zabezpečení signalizace v vyvíjejících se sítích 3GPP, zejména s nástupem plně IP služeb jako Voice over LTE (VoLTE) a IMS. Před jeho formalizací existovaly mechanismy ochrany signalizace, ale často spoléhaly na implicitní asociace klíčů nebo méně podrobné identifikátory, což mohlo vést k nejednoznačnostem při výběru klíče během předávání služby nebo přechodů mezi službami. To bylo obzvláště problematické v IMS, kde signalizace SIP vyžaduje silnou ochranu integrity, aby se zabránilo podvodům a zneužívání služeb. SPK-ID poskytuje standardizovaný způsob, jak označit a odkazovat na konkrétní klíčový materiál, čímž řeší problém efektivní správy více bezpečnostních kontextů pro jedno UE.

Historicky, jak sítě přecházely z jader s přepojováním okruhů na jádra s přepojováním paketů, se signalizační útoky staly proveditelnějšími kvůli zvýšené expozici provozu řídicí roviny přes IP sítě. Vytvoření SPK-ID bylo motivováno požadavkem ve 3GPP Release 14 na vylepšení bezpečnostního rámce pro IMS a později pro 5G Core, aby bylo zajištěno, že ochrana signalizace může škálovat s novými případy použití, jako je síťové dělení (network slicing) a edge computing. Řeší omezení předchozích přístupů tím, že umožňuje explicitní svázání klíče s jeho kontextem použití, což zlepšuje jasnost zabezpečení a napomáhá při odstraňování problémů a auditu. Bez takového identifikátoru by sítě mohly zápasit s problémy synchronizace klíčů během událostí mobility nebo když UE přistupuje k více simultánním službám, z nichž každá má odlišné bezpečnostní požadavky.

## Klíčové vlastnosti

- Jednoznačně identifikuje klíčový kontext pro zabezpečení signalizace pro UE
- Umožňuje ochranu integrity a důvěrnosti pro signalizaci NAS a IMS
- Podporuje efektivní správu a získávání klíčů během předávání relace
- Umožňuje více souběžných bezpečnostních kontextů pro různé služby
- Integruje se s 3GPP procedurami Authentication and Key Agreement (AKA)
- Specifikován napříč specifikacemi protokolů jádra sítě a IMS pro interoperabilitu

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems

---

📖 **Anglický originál a plná specifikace:** [SPK-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/spk-id/)
