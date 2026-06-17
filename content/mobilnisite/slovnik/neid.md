---
slug: "neid"
url: "/mobilnisite/slovnik/neid/"
type: "slovnik"
title: "NEID – Network Element Identifier"
date: 2025-01-01
abbr: "NEID"
fullName: "Network Element Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/neid/"
summary: "NEID (Network Element Identifier, identifikátor síťového prvku) je jedinečný identifikátor používaný v rámci bezpečnostních a řídicích rámců 3GPP k jednoznačné identifikaci konkrétního síťového prvku,"
---

NEID je jedinečný identifikátor používaný v rámci specifikací 3GPP k jednoznačné identifikaci konkrétního síťového prvku, jako je základnová stanice nebo uzel jádra sítě, pro účely zabezpečené komunikace, auditování a správy poruch.

## Popis

NEID (Network Element Identifier, identifikátor síťového prvku) je základní identifikátor definovaný ve specifikacích 3GPP, zejména v bezpečnostním kontextu (TS 33.108). Slouží jako globálně nebo v rámci domény jedinečný název pro síťový prvek ([NE](/mobilnisite/slovnik/ne/)), který se účastní bezpečnostních a řídicích protokolů definovaných 3GPP. Síťovým prvkem může být jakýkoli fyzický nebo logický uzel v systému, například komponenta rádiového přístupového sítě (RAN) jako gNB nebo eNodeB, funkce jádra sítě (CN) jako [AMF](/mobilnisite/slovnik/amf/) nebo [SMF](/mobilnisite/slovnik/smf/), nebo entita provozu a údržby (O&M) jako Element Manager ([EM](/mobilnisite/slovnik/em/)) nebo Network Manager ([NM](/mobilnisite/slovnik/nm/)).

NEID se používá jako primární identifikátor v bezpečnostních mechanismech, především v architekturách 3GPP pro zákonné odposlechy ([LI](/mobilnisite/slovnik/li/)) a navázání klíčů (KE). V systémech LI slouží NEID k jednoznačné identifikaci síťového prvku, který generuje nebo zprostředkovává informace související s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) a obsah komunikace ([CC](/mobilnisite/slovnik/cc/)). To umožňuje funkci správy zákonných odposlechů (LIAF) a mediačním funkcím správně přiřadit odposlechnutá data jejich zdroji. V protokolech pro navázání klíčů za účelem zabezpečení řídicích rozhraní (jako je protokol KE definovaný v TS 33.310) tvoří NEID součást jména subjektu certifikátu nebo je použit při autentizačních výměnách, aby se zajistilo, že klíče jsou navázány se správným, zamýšleným síťovým prvkem.

Z provozní perspektivy je struktura a přidělování NEID klíčové pro správu sítě. Umožňují systémům správy poruch přesně určit zařízení hlásící alarm, systémům správy výkonnosti korelovat metriky ze správného zdroje a systémům správy konfigurace přesně cílit aktualizace. NEID musí být během životního cyklu prvku trvalý a stabilní. Jeho formát je často hierarchický a může zahrnovat prvky jako identifikátor veřejné pozemní mobilní sítě (PLMN ID), identifikátory přiřazené operátorem a čísla typu nebo instance zařízení, což zajišťuje jedinečnost i v potenciálně globálních nasazeních a usnadňuje automatickou detekci a inventarizaci.

## K čemu slouží

NEID byl vytvořen, aby řešil kritickou potřebu jednoznačné identifikace ve velkých, více-dodavatelských a potenciálně propojených telekomunikačních sítích. Před zavedením standardizovaných identifikátorů používali operátoři a dodavatelé zařízení proprietární systémy pojmenování, což komplikovalo interoperabilitu, zabezpečení a centralizovanou správu, zejména v sítích složených ze zařízení různých dodavatelů.

Jeho primárním účelem je řešit problém identifikace ve dvou klíčových oblastech: zabezpečení a spravovatelnosti. Pro zabezpečení vyžadují protokoly jako zákonný odposlech a zabezpečená výměna klíčů důvěryhodný, nefalšovatelný identifikátor, který váže bezpečnostní přihlašovací údaje (jako digitální certifikáty) a odposlechnutá data ke konkrétní fyzické nebo logické entitě. Bez jedinečného NEID by nebylo možné spolehlivě ověřit síťový prvek žádající o zabezpečené spojení nebo auditovat zdroj odposlechnuté komunikace, což by ohrožovalo právní shodu a integritu sítě. Pro správu sítě poskytuje NEID stabilní klíč pro všechny funkce O&M. Umožňuje operátorovu systému správy sítě (NMS) jednoznačně identifikovat a komunikovat s tisíci různorodými prvky, což umožňuje automatizované zřizování, softwarové aktualizace, korelaci poruch a monitorování výkonnosti napříč celou sítí bez ohledu na dodavatele použitého zařízení.

## Klíčové vlastnosti

- Globálně nebo v rámci domény jedinečný identifikátor pro fyzický nebo logický síťový prvek
- Používá se jako identifikátor subjektu v bezpečnostních certifikátech (např. pro TLS na řídicích rozhraních)
- Povinný identifikátor v architekturách 3GPP pro zákonné odposlechy (LI) pro přiřazení odposlechnutých dat
- Umožňuje přesné cílení v protokolech správy sítě (poruchy, konfigurace, výkonnost)
- Podporuje interoperabilitu mezi více dodavateli díky standardizovanému systému pojmenování
- Trvalý identifikátor, který zůstává konstantní po celý provozní životní cyklus prvku

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [NEID na 3GPP Explorer](https://3gpp-explorer.com/glossary/neid/)
