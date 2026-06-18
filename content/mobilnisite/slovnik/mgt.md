---
slug: "mgt"
url: "/mobilnisite/slovnik/mgt/"
type: "slovnik"
title: "MGT – Mobile Global Title"
date: 2025-01-01
abbr: "MGT"
fullName: "Mobile Global Title"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mgt/"
summary: "Jedinečná adresa používaná v jádrové síti založené na SS7/SIGTRAN k identifikaci a směrování signalizačních zpráv k entitám mobilní sítě, jako jsou HLR, MSC nebo SGSN. Je klíčová pro zajištění spolehl"
---

MGT je jedinečná adresa SS7/SIGTRAN používaná k identifikaci a směrování signalizačních zpráv k entitám mobilní sítě, jako jsou HLR, MSC nebo SGSN, pro spolehlivou signalizaci a správu účastníků v rámci celé sítě.

## Popis

Mobile Global Title (MGT, mobilní globální titul) je klíčový adresní mechanismus v rámci architektur Signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)) a SIGTRAN používaných jádrovými sítěmi 2G (GSM), 3G (UMTS) a raného 4G (EPS). Funguje jako jedinečná směrovatelná adresa pro síťové elementy, které zajišťují správu mobility a řízení hovorů/sezení, jako je Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)). MGT není identifikátor účastníka jako [IMSI](/mobilnisite/slovnik/imsi/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/); místo toho identifikuje samotný síťový uzel. Je strukturován dle doporučení ITU-T a typicky zahrnuje prvky jako kód země, kód sítě a jedinečný identifikátor konkrétního uzlu, což umožňuje signalizačním přenosovým bodům (STP) provádět překlad globálního titulu (GTT) a přesně směrovat zprávy přes mezinárodní a národní sítě.

Z architektonického hlediska je MGT vložen do adresních polí signalizačních jednotek zpráv SS7 (MSU), konkrétně do adresy volaného (CdPA) nebo volajícího (CgPA) účastníka v rámci Signalizačního spojového řídicího subsystému (SCCP). Když je třeba odeslat signalizační zprávu, například požadavek na aktualizaci polohy nebo dotaz na zřízení hovoru, do HLR, zdrojový uzel použije MGT příslušného HLR jako cílovou adresu. Mezilehlé STP analyzují tento MGT. Prostřednictvím procesu zvaného Global Title Translation (GTT) STP konzultuje své směrovací tabulky, aby namapoval logickou adresu MGT na skutečný cílový kód bodu (DPC) a číslo subsystému (SSN) cílového uzlu, což umožňuje skokové směrování signalizační sítí. Tato vrstva abstrakce poskytuje významnou flexibilitu, umožňuje přečíslování síťových elementů, vyvažování zátěže a redundanci, aniž by bylo nutné, aby každý uzel v síti znal fyzický kód bodu každého dalšího uzlu.

Role MGT je zásadní pro všechny procedury mobility a správy účastníků. Například když se mobilní telefon přihlásí do nové sítě (roaming), musí Visitor Location Register (VLR) kontaktovat Home Location Register (HLR) účastníka, aby jej autentizoval a načetl jeho profil. VLR k adresování signalizační zprávy použije MGT příslušného HLR, který je často odvozen z IMSI účastníka. Podobně doručování SMS mezi sítěmi spoléhá na MGT pro směrování zpráv ke správnému Short Message Service Center (SMSC) nebo MSC. S vývojem sítí směrem k plně IP architekturám s protokolem Diameter v 4G a HTTP/2 v 5G role SS7 a MGT poklesla, byly nahrazeny plně kvalifikovanými doménovými jmény (FQDN) a IP adresami. Pro interoperabilitu se staršími sítěmi a pro některé regulační služby, jako je zákonné odposlouchávání, však zůstává pochopení směrování založeného na MGT pro telekomunikační inženýry nezbytné.

## K čemu slouží

Mobile Global Title byl vytvořen, aby vyřešil základní problém škálovatelného a flexibilního adresování a směrování v globálních, více-dodavatelských a více-operátorských telekomunikačních signalizačních sítích. Před standardizovanými globálními tituly bylo síťové adresování často založeno pouze na kódech bodů (point codes), což jsou číselné identifikátory smysluplné pouze v rámci konkrétní sítě nebo signalizačního prostoru kódů bodů. To činilo mezinárodní a mezioperátorské směrování složitým a nepružným, protože každý uzel by potřeboval kompletní mapování kódů bodů všech ostatních uzlů. MGT zavedl logickou, strukturovanou adresu, která je nezávislá na fyzické topologii sítě.

Primární motivací bylo umožnit bezproblémovou globální mobilitu a interoperabilitu. Jak se GSM rozšiřovalo z evropského standardu na celosvětový systém, byl potřebný mechanismus, který by umožnil libovolnému síťovému uzlu lokalizovat domovskou databázi účastníka (HLR) kdekoli na světě na základě informací obsažených v identitě účastníka (IMSI). MGT, odvozený z Mobile Country Code (MCC) a Mobile Network Code (MNC) z IMSI, poskytuje tuto logickou vazbu. Umožňuje navštívené síti sestavit adresu pro HLR domovské sítě bez předchozí znalosti fyzického umístění tohoto HLR v síti. Toto oddělení logické identity od fyzických směrovacích informací prostřednictvím Global Title Translation na STP je tím, co umožnilo komerční a technickou proveditelnost rozsáhlého automatizovaného roamingu. Řešilo to omezení rigidního směrování pouze na bázi kódů bodů a poskytlo adresní flexibilitu nezbytnou pro růst sítě, přemisťování databází a implementaci bránových a firewallových funkcí ve signalizační síti.

## Klíčové vlastnosti

- Globálně jedinečná logická adresa pro uzly jádrové sítě
- Umožňuje směrování na základě identity účastníka (např. odvozené z IMSI)
- Odděluje logické adresování od fyzické topologie sítě (kódy bodů)
- Nezbytná pro signalizaci založenou na SS7/SIGTRAN v sítích 2G, 3G a raného 4G
- Podporuje Global Title Translation (GTT) na Signalizačních přenosových bodech (STP)
- Základní prvek pro mezinárodní roaming a signalizaci mezi operátory

## Související pojmy

- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements

---

📖 **Anglický originál a plná specifikace:** [MGT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mgt/)
