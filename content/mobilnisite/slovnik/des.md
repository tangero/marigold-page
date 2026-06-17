---
slug: "des"
url: "/mobilnisite/slovnik/des/"
type: "slovnik"
title: "DES – Data Encryption Standard"
date: 2025-01-01
abbr: "DES"
fullName: "Data Encryption Standard"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/des/"
summary: "Symetrický blokový šifrovací algoritmus používaný v raných specifikacích 3GPP pro šifrování uživatelských dat a signalizace. Poskytoval důvěrnost pro okruhově přepínané služby a určité autentizační me"
---

DES je zastaralý symetrický blokový šifrovací algoritmus používaný v raných specifikacích 3GPP k zajištění důvěrnosti (confidentiality) pro okruhově přepínaná uživatelská data, signalizaci a určité autentizační mechanismy.

## Popis

Data Encryption Standard (DES) je symetrická bloková šifra, která pracuje s 64bitovými bloky dat pomocí 56bitového klíče. V systémech 3GPP byl DES implementován jako kryptografický primitiv pro zajištění důvěrnosti dat, především v raných vydáních pro zabezpečení provozu v uživatelské rovině v okruhově přepínaných doménách a v rámci specifických bezpečnostních protokolů. Algoritmus využívá strukturu Feistelovy sítě sestávající z 16 kol permutačních a substitučních operací. Každé kolo používá jiný 48bitový podklíč odvozený z původního 56bitového klíče pomocí plánu klíčů. Základní operace zahrnují expanzi, substituci pomocí S-boxů, permutaci a XOR s klíčem kola, což poskytuje záměnu (confusion) a rozptyl (diffusion) otevřeného textu.

V architektuře 3GPP byl DES integrován do bezpečnostních funkcí v jádrové síti a v některých raných implementacích také pro šifrování přes rádiové rozhraní. Byl například specifikován pro použití v proudových šifrách [A5/1](/mobilnisite/slovnik/a5-1/) a [A5/2](/mobilnisite/slovnik/a5-2/) pro GSM, které odvozovaly šifrovací proudy na principech DES pro šifrování hlasu a dat přes rádiové rozhraní. V jádrové síti mohl být DES využit v protokolech pro zabezpečení signalizačních zpráv nebo pro šifrování dat přenášených mezi síťovými prvky, jako je například mezi Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)). Provoz algoritmu byl typicky řízen bezpečnostními moduly v síťových uzlech, což zajišťovalo ochranu citlivých informací před odposlechem.

Navzdory své historické roli technická omezení DES, zejména jeho krátká délka klíče, učinila algoritmus zranitelným vůči útokům vyčerpávajícím prohledáváním klíčového prostoru. To vedlo 3GPP k postupnému vyřazení DES ve prospěch varianty Triple DES (3DES), která aplikuje algoritmus DES třikrát s dvěma nebo třemi různými klíči, čímž efektivně zvyšuje sílu klíče na 112 nebo 168 bitů. Nicméně i 3DES byl v pozdějších vydáních z velké části nahrazen standardem Advanced Encryption Standard ([AES](/mobilnisite/slovnik/aes/)) díky jeho vyšší bezpečnosti a efektivitě. Zařazení DES do specifikací 3GPP sloužilo jako základní kryptografická metoda, ale jeho odsunutí zdůrazňuje vývoj směrem k robustnějším bezpečnostním mechanismům v mobilních sítích.

## K čemu slouží

DES byl začleněn do raných standardů 3GPP, aby poskytl standardizovanou metodu pro šifrování uživatelských dat a signalizace, a řešil tak potřebu důvěrnosti v mobilní komunikaci. Před jeho přijetím mnohé telekomunikační systémy postrádaly robustní, interoperabilní šifrování, což ponechávalo hlasové hovory a datové přenosy zranitelné vůči zachycení. DES nabídl důkladně prověřený, vládou standardizovaný algoritmus, který mohl být implementován v síťových zařízeních od různých výrobců, a zajišťoval tak základní úroveň zabezpečení pro okruhově přepínané služby, jako jsou hlasové hovory v sítích GSM a raných sítích UMTS.

Vznik DES byl motivován rostoucím povědomím o problémech soukromí v bezdrátové komunikaci a nutností ochrany před odposlechem na rádiových spojích. V kontextu 3GPP řešil problém zabezpečení provozu přes rádiové rozhraní mezi mobilním zařízením a základnovou stanicí, stejně jako backhaulových spojů uvnitř sítě. Šifrováním datových proudů DES pomáhal zabránit neoprávněnému přístupu k citlivým informacím, čímž zvyšoval důvěru uživatelů a naplňoval regulační požadavky na ochranu dat. Jeho použití v autentizačních a dohodovacích protokolech klíčů také přispělo k celkovému bezpečnostnímu rámci raných buněčných systémů.

Účel DES byl však nakonec podlomen pokrokem ve výpočetním výkonu, který učinil jeho 56bitový klíč zranitelným vůči útokům hrubou silou. Toto omezení vedlo 3GPP k přechodu na silnější algoritmy, ale počáteční implementace DES položila základy kryptografické bezpečnosti v mobilních sítích, demonstrovala význam šifrování v telekomunikacích a připravila cestu pro pokročilejší standardy, jako je [AES](/mobilnisite/slovnik/aes/).

## Klíčové vlastnosti

- Symetrická bloková šifra s délkou klíče 56 bitů
- Pracuje s 64bitovými datovými bloky pomocí struktury Feistelovy sítě
- Poskytuje důvěrnost dat prostřednictvím šifrovacích a dešifrovacích funkcí
- Využívá 16 kol permutace a substituce pro zabezpečení
- Integrována do raných specifikací 3GPP pro šifrování okruhově přepínaných služeb
- Podporována v protokolech jako A5/1 a A5/2 pro zabezpečení rádiového rozhraní GSM

## Související pojmy

- [AES – Advanced Encryption Standard](/mobilnisite/slovnik/aes/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 31.114** (Rel-8) — USAT Interpreter Transmission Protocol
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report

---

📖 **Anglický originál a plná specifikace:** [DES na 3GPP Explorer](https://3gpp-explorer.com/glossary/des/)
