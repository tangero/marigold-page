---
slug: "csrn"
url: "/mobilnisite/slovnik/csrn/"
type: "slovnik"
title: "CSRN – Circuit Switched Routing Number"
date: 2025-01-01
abbr: "CSRN"
fullName: "Circuit Switched Routing Number"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/csrn/"
summary: "Dočasný identifikátor přiřazený mobilnímu účastníkovi během procedur přepojení na okruhovou komutaci (CSFB) při provozu v sítích LTE/EPC. Umožňuje směrování hlasových hovorů s okruhovou komutací přes"
---

CSRN je dočasný identifikátor přiřazený mobilnímu účastníkovi během procedur přepojení na okruhovou komutaci (circuit-switched fallback), který umožňuje směrování hlasových hovorů přes starší 2G/3G sítě, zatímco zařízení zůstává v LTE pro přenos dat.

## Popis

Circuit Switched Routing Number (CSRN) je klíčový síťový identifikátor definovaný ve specifikacích 3GPP, který umožňuje funkci přepojení na okruhovou komutaci ([CSFB](/mobilnisite/slovnik/csfb/)) v sítích LTE/EPC. Když se mobilní zařízení schopné provozu v LTE (pouze paketová komutace) i starších 2G/3G sítích (okruhová komutace) registruje v síti LTE, může mu entita [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity) přiřadit CSRN. Toto číslo slouží jako dočasná směrovací adresa v doméně s okruhovou komutací, což umožňuje síti správně směrovat příchozí hlasové hovory na příslušný ústřednový uzel [MSC](/mobilnisite/slovnik/msc/) (mobile switching center) obsluhující aktuální polohu účastníka.

CSRN funguje v rámci architektury CSFB, kde MME komunikuje s MSC Serverem přes rozhraní SGs. Když dorazí hovor pro účastníka připojeného k LTE, MSC použije CSRN k identifikaci konkrétní entity MME, která tohoto účastníka obsluhuje. CSRN typicky dodržuje číslovací formát E.164 a je strukturován tak, aby obsahoval směrovací informace, které nasměrují hovor přes správné síťové prvky. MME ukládá CSRN ve spojení s mezinárodním identifikátorem mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)) a dalšími kontextovými informacemi a toto mapování udržuje po dobu trvání CSFB relace.

Během procedur CSFB, když je potřeba navázat hlasový hovor, MME použije CSRN ke koordinaci s MSC pro volání (paging) a přípravu předání spojení. CSRN umožňuje MSC korelovat příchozí hovor s okruhovou komutací s konkrétním LTE kontextem udržovaným v MME. Tato koordinace je zásadní pro spuštění procedury přepojení, při které UE dočasně opustí pokrytí LTE, aby navázalo hlasový hovor v 2G/3G sítích. CSRN zůstává platný, dokud se účastník od sítě neodpojí nebo není CSFB kontext vymazán, poté může být přidělen jinému účastníkovi.

Implementace CSRN podporuje různé scénáře CSFB včetně příchozích a odchozích hovorů, stejně jako různé metody přepojení, jako je přesměrování (redirection), předání spojení (handover) nebo příkaz ke změně buňky (cell change order). Role CSRN přesahuje pouhou identifikaci – umožňuje síti zachovat kontinuitu služeb a správné záznamy pro účtování během mezisystémové mobility mezi doménami s paketovou a okruhovou komutací. Tento identifikátor byl obzvláště důležitý v raných nasazeních LTE, kde hlasové služby silně závisely na mechanismech přepojení, než se široce rozšířilo VoLTE.

## K čemu slouží

CSRN byl vytvořen, aby řešil zásadní výzvu poskytování hlasových služeb v raných sítích LTE, kterým chyběly nativní schopnosti okruhové komutace. LTE bylo navrženo jako čistě paketově komutovaná síť optimalizovaná pro datové služby, což ponechalo mezeru pro tradiční hlasové hovory s okruhovou komutací. CSRN umožňuje operátorům využít jejich stávající infrastrukturu 2G/3G pro hlasové služby, zatímco zavádějí LTE pro vylepšené datové možnosti, což poskytuje hladkou přechodovou cestu bez nutnosti okamžité investice do řešení VoLTE založených na IMS.

Před mechanismy [CSFB](/mobilnisite/slovnik/csfb/) s řádnými identifikátory, jako je CSRN, musela duální zařízení periodicky skenovat 2G/3G sítě, aby přijímala služby s okruhovou komutací, což vedlo ke zvýšené spotřebě baterie a potenciálním zmeškaným hovorům. CSRN to řeší tím, že umožňuje síti LTE udržovat přehled o okruhovém kontextu účastníka a efektivně koordinovat procedury přepojení pouze v případě potřeby. Tento přístup zachoval uživatelský zážitek 'vždy dostupné' hlasové služby a zároveň maximalizoval čas strávený v efektivnější síti LTE pro datové služby.

Vytvoření CSRN řešilo konkrétní technická omezení v raných řešeních mezisystémové mobility. Předchozí přístupy buď vyžadovaly složité implementace s duálním rádiem, nebo trpěly nadměrnou signalizační režií a zpožděním při sestavování hovorů. Tím, že poskytl standardizovaný dočasný identifikátor, na který se mohly odkazovat prvky sítí s paketovou i okruhovou komutací, CSRN umožnil efektivnější koordinaci mezi [MME](/mobilnisite/slovnik/mme/) a [MSC](/mobilnisite/slovnik/msc/), snížil latenci přepojení a zlepšil celkovou spolehlivost systému během kritického přechodného období od architektur hlasu s okruhovou komutací k paketové komutaci.

## Klíčové vlastnosti

- Dočasný identifikátor ve formátu E.164 pro směrování v okruhové komutaci
- Umožňuje korelaci mezi kontextem LTE/EPC a doménou s okruhovou komutací
- Podporuje procedury CSFB pro příchozí i odchozí hovory
- Usnadňuje efektivní koordinaci volání (paging) mezi MME a MSC
- Zachovává zpětnou kompatibilitu se staršími hlasovými sítěmi 2G/3G
- Umožňuje správné účtování a billing během mezisystémové mobility

## Související pojmy

- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [EPS – Evolved Packet System](/mobilnisite/slovnik/eps/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TS 23.206** (Rel-7) — Voice Call Continuity (VCC) Functional Architecture
- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol

---

📖 **Anglický originál a plná specifikace:** [CSRN na 3GPP Explorer](https://3gpp-explorer.com/glossary/csrn/)
