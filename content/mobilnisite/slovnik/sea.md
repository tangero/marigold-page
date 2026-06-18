---
slug: "sea"
url: "/mobilnisite/slovnik/sea/"
type: "slovnik"
title: "SEA – SS7 security gateway Encryption Algorithm identifier"
date: 2025-01-01
abbr: "SEA"
fullName: "SS7 security gateway Encryption Algorithm identifier"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sea/"
summary: "Parametr používaný ve specifikacích zabezpečení 3GPP k identifikaci konkrétního dohodnutého šifrovacího algoritmu pro použití mezi Bezpečnostní bránou (SEG) a jinou síťovou entitou v IP prostředí NDS/"
---

SEA je parametr zabezpečení 3GPP, který identifikuje dohodnutý šifrovací algoritmus pro zabezpečení signalizačního provozu mezi Bezpečnostní bránou (Security Gateway) a jinou entitou v prostředí NDS/IP.

## Popis

Identifikátor šifrovacího algoritmu Bezpečnostní brány [SS7](/mobilnisite/slovnik/ss7/) (SEA) je specifický parametr definovaný v rámci architektury zabezpečení síťové domény ([NDS](/mobilnisite/slovnik/nds/)) 3GPP, určený zejména pro zabezpečení signalizace založené na systému č. 7 (SS7). [NDS/IP](/mobilnisite/slovnik/nds-ip/) poskytuje zabezpečení pro provoz řídicí roviny založený na IP mezi síťovými doménami (např. mezi sítěmi dvou různých operátorů nebo mezi různými bezpečnostními doménami v síti jednoho operátora). Bezpečnostní brány ([SEG](/mobilnisite/slovnik/seg/)) jsou entity, které implementují bezpečnostní funkce NDS/IP, primárně [IPsec](/mobilnisite/slovnik/ipsec/).

Když dvě SEG navážou zabezpečený IPsec tunel pro ochranu signalizačního provozu (který může být SS7-over-IP, jako SIGTRAN, nebo Diameter/[SIP](/mobilnisite/slovnik/sip/)), musí vyjednat používané bezpečnostní asociace ([SA](/mobilnisite/slovnik/sa/)). Toto vyjednávání zahrnuje výběr konkrétních kryptografických algoritmů pro ochranu integrity a důvěrnosti (šifrování). SEA je identifikátor používaný k určení, *který* šifrovací algoritmus byl pro použití v daném zabezpečeném tunelu dohodnut. Je součástí dat bezpečnostní asociace, která musí být konzistentně nakonfigurována a rozpoznána oběma partnerskými SEG, aby byla zajištěna interoperabilita a úspěšné dešifrování provozu.

Hodnota SEA odpovídá konkrétnímu šifrovacímu algoritmu definovanému v příslušné specifikaci zabezpečení 3GPP (TS 33.204). Může například odkazovat na algoritmy jako AES-CBC nebo 3DES. SEA spolu s dalšími identifikátory pro algoritmy integrity (jako [SPI](/mobilnisite/slovnik/spi/) - Security Parameter Index, ačkoli SPI je obecnější) umožňuje SEG správně zpracovat příchozí chráněné pakety aplikací správného dešifrovacího algoritmu. Jeho použití je klíčové v prostředí s více dodavateli nebo tam, kde síťoví operátoři mohou podporovat sadu algoritmů s různou sílou, což umožňuje jasnou a jednoznačnou dohodu o algoritmu použitém pro konkrétní spojení.

## K čemu slouží

SEA existuje za účelem řešení problému vyjednávání a identifikace algoritmu standardizovaným a interoperabilním způsobem pro zabezpečení signalizace SS7 přes IP sítě. Jak se jádrové sítě vyvíjely od tradičního SS7 založeného na TDM k přenosu založenému na IP (pomocí SIGTRAN), staly se signalizační spoje zranitelnými vůči útokům založeným na IP, jako je odposlech a modifikace zpráv. Architektura NDS/IP byla vytvořena k aplikaci ochrany IPsec na tento provoz.

Klíčovou výzvou v jakémkoli nasazení IPsec je zajistit, aby oba konce bezpečnostní asociace používaly stejné kryptografické algoritmy. Bez standardizovaného identifikátoru by různí dodavatelé nebo síťové konfigurace mohli odkazovat na stejný algoritmus různými názvy nebo parametry, což by vedlo k selhání spojení. SEA poskytuje v kontextu 3GPP pro bezpečnostní brány SS7 specifický, dohodnutý token. Řeší omezení ad-hoc nebo proprietárních mechanismů výběru algoritmu a zajišťuje, že když SEG v jedné síťové doméně naváže tunel se SEG v jiné doméně, mohou jednoznačně identifikovat šifrovací algoritmus, který má být použit, což umožňuje úspěšnou zabezpečenou komunikaci a zachovává důvěrnost signalizačních zpráv procházejících rozhraním mezi operátory.

## Klíčové vlastnosti

- Jednoznačně identifikuje šifrovací algoritmus pro IPsec bezpečnostní asociaci mezi SEG.
- Definován v rámci architektury NDS/IP 3GPP (TS 33.204).
- Nezbytný pro interoperabilitu mezi bezpečnostními branami od více dodavatelů.
- Používá se v kontextu zabezpečení signalizace založené na SS7 přes IP sítě (SIGTRAN).
- Součást parametrů bezpečnostní asociace, které jsou vyjednány nebo předem nakonfigurovány.
- Zajišťuje konzistentní proces dešifrování na přijímající SEG.

## Související pojmy

- [NDS/IP – Network Domain Security for IP based Protocols](/mobilnisite/slovnik/nds-ip/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)

## Definující specifikace

- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [SEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sea/)
