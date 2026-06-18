---
slug: "ssl"
url: "/mobilnisite/slovnik/ssl/"
type: "slovnik"
title: "SSL – Secure Socket Layer"
date: 2026-01-01
abbr: "SSL"
fullName: "Secure Socket Layer"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ssl/"
summary: "Kryptografický protokol navržený k zajištění zabezpečené komunikace po počítačové síti, zejména internetu. Zajišťuje soukromí, autentizaci a integritu dat mezi dvěma komunikujícími aplikacemi, napříkl"
---

SSL je kryptografický protokol navržený k zajištění zabezpečené komunikace, která zaručuje soukromí, autentizaci a integritu dat mezi dvěma komunikujícími aplikacemi po síti.

## Popis

Secure Socket Layer (SSL) je protokolová vrstva fungující nad transportní vrstvou TCP, která poskytuje bezpečnostní služby pro aplikační protokoly jako [HTTP](/mobilnisite/slovnik/http/), čímž vzniká [HTTPS](/mobilnisite/slovnik/https/). Jejím hlavním cílem je vytvoření šifrovaného spojení mezi klientem a serverem, které zajistí, že všechna přenášená data zůstanou soukromá a nezměněná. Protokol SSL zahrnuje fázi handshake, během které se klient a server vzájemně autentizují (často pouze autentizace serveru) a vyjednávají kryptografické algoritmy a relakční klíče, které budou použity. Následuje fáze záznamového protokolu, ve které jsou aplikační data zašifrována, ověřena pomocí kódu pro ověření zprávy ([MAC](/mobilnisite/slovnik/mac/)) a přenesena.

Architektonicky je SSL (a jeho nástupce [TLS](/mobilnisite/slovnik/tls/)) implementován jako mezivrstva mezi aplikační a transportní vrstvou. Ve specifikacích 3GPP je SSL uváděn jako metoda pro zabezpečení různých rozhraní, zejména pro provozní a správní (O&M) provoz, data uživatelské roviny v určitých přenosech nebo pro zabezpečení webových rozhraní síťových prvků. Protokol používá kombinaci asymetrické kryptografie (jako [RSA](/mobilnisite/slovnik/rsa/) nebo Diffie-Hellman) pro výměnu klíčů a autentizaci a symetrické kryptografie (jako [AES](/mobilnisite/slovnik/aes/) nebo 3DES) pro hromadné šifrování dat. Kritickou součástí je použití digitálních certifikátů X.509 vydaných certifikační autoritou ([CA](/mobilnisite/slovnik/ca/)) k ověření identity komunikujících stran.

V rámci sítě 3GPP může být SSL nasazen pro zabezpečení rozhraní založených na HTTP používaných pro správu zařízení (např. [OMA](/mobilnisite/slovnik/oma/) DM), pro zabezpečení komunikace mezi uživatelským zařízením (UE) a síťovým aplikačním serverem nebo pro ochranu správního provozu k síťovým prvkům, jako jsou eNB nebo MME, a od nich. Protokol zvládá obnovení relace za účelem zlepšení výkonu tím, že se vyhne úplnému handshake pro opakovaná spojení. Zatímco SSL v3.0 byla poslední verzí původního protokolu SSL, je z velké části zastaralá a nahrazena protokolem Transport Layer Security (TLS), který je založen na SSL, ale obsahuje bezpečnostní vylepšení a je termínem běžněji používaným v pozdějších vydáních 3GPP, ačkoli funkční koncept zůstává stejný.

## K čemu slouží

SSL byl vytvořen, aby řešil zásadní nedostatek zabezpečení v raných internetových protokolech, které přenášely data, včetně citlivých informací jako hesla a čísla kreditních karet, v nešifrované podobě. Jeho vývoj byl motivován potřebou elektronického obchodu a zabezpečených online transakcí v 90. letech 20. století. Pro sítě 3GPP začlenění SSL (a později TLS) poskytlo standardizovanou, široce implementovanou metodu pro zabezpečení datových komunikací, které procházejí potenciálně nedůvěryhodnými sítěmi, jako je veřejný internet mezi UE a poskytovatelem služeb nebo mezi systémy správy síťových operátorů.

Protokol vyřešil klíčové problémy odposlechu, manipulace a padělání zpráv pro služby založené na IP nabízené přes mobilní sítě. Před rozšířeným používáním SSL/TLS vyžadovalo zabezpečení aplikačních dat proprietární řešení nebo bylo zanedbáváno, což vytvářelo zranitelnosti. V kontextu 3GPP, když sítě začaly nabízet služby založené na IP (IMS), správu zařízení a později webová API pro správu sítě, přijetí známého bezpečnostního protokolu jako SSL zajistilo interoperabilitu a vysokou úroveň jistoty. Řešilo to omezení zabezpečení na nižších vrstvách (např. IPsec), které mohlo být složitější na nasazení pro konkrétní aplikační toky, a poskytlo známý bezpečnostní model pro vývojáře aplikací.

## Klíčové vlastnosti

- Poskytuje šifrování pro důvěrnost dat pomocí symetrických šifer
- Zajišťuje integritu zpráv pomocí klíčových kódů pro ověření zprávy (MAC)
- Podporuje autentizaci serveru (a volitelně i klienta) pomocí certifikátů X.509
- Vyjednává kryptografické parametry prostřednictvím definovaného handshake protokolu
- Umožňuje obnovení relace za účelem snížení režie při navazování spojení
- Funguje transparentně pro nadřazenou aplikační vrstvu

## Související pojmy

- [TLS – Transport Layer Security](/mobilnisite/slovnik/tls/)
- [HTTPS – Hyper Text Transfer Protocol Secure](/mobilnisite/slovnik/https/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 31.112** (Rel-8) — USAT Interpreter System Architecture
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.583** (Rel-19) — HNB OAM&P Procedure Flows for Type 1 Interface
- **TS 32.593** (Rel-19) — HeNB OAM&P Procedure Flows for Type 1 Interface
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [SSL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssl/)
