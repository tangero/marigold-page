---
slug: "ber-tlv"
url: "/mobilnisite/slovnik/ber-tlv/"
type: "slovnik"
title: "BER-TLV – Basic Encoding Rules - Tag Length Value"
date: 2025-01-01
abbr: "BER-TLV"
fullName: "Basic Encoding Rules - Tag Length Value"
category: "Protocol"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ber-tlv/"
summary: "BER-TLV je standardizovaný formát kódování dat používaný ve specifikacích 3GPP, zejména pro aplikace čipových karet, jako jsou USIM. Strukturovaně uspořádává data do tagu (identifikující datový objekt"
---

BER-TLV je standardizovaný formát kódování dat používaný ve specifikacích 3GPP, který strukturovaně uspořádává data do tagu (značky), délky a hodnoty pro spolehlivou výměnu v aplikacích čipových karet, jako jsou USIM.

## Popis

BER-TLV je základní schéma kódování dat odvozené od základních pravidel kódování ASN.1 (Abstract Syntax Notation One). Poskytuje strukturovanou metodu pro reprezentaci složitých datových objektů jako sekvenčního proudu bajtů, což umožňuje interoperabilitu mezi různými systémy. Kódování dodržuje striktní formát tripletu: pole Tag (značka), pole Length (délka) a pole Value (hodnota). Tag je jedinečný identifikátor klasifikující datový objekt, který udává jeho typ, třídu (univerzální, aplikační, kontextově specifickou nebo privátní) a zda je primitivní (jednoduchá data) nebo konstruovaný (obsahuje vnořené TLV objekty). Pole Length určuje velikost pole Value v bajtech, přičemž používá buď kódování určité, nebo neurčité délky. Pole Value obsahuje vlastní datovou náplň, která může být jednoduchá binární data, nebo v případě konstruovaných tagů zřetězená série vnořených datových objektů BER-TLV.

V systémech 3GPP je BER-TLV podrobně specifikován v technických specifikacích, jako je 3GPP TS 31.102 (Charakteristiky aplikace Universal Subscriber Identity Module (USIM)) a TS 31.103 (Charakteristiky aplikace IP Multimedia Services Identity Module ([ISIM](/mobilnisite/slovnik/isim/))). Je to primární kódovací mechanismus pro příkazy a odpovědi vyměňované mezi mobilním zařízením ([ME](/mobilnisite/slovnik/me/)) a čipem UICC, který hostuje USIM/ISIM. To zahrnuje příkazy pro přístup k souborům, autentizaci a správu aplikací a služeb. Protokol funguje přes logický kanál zřízený mezi terminálem a kartou, což zajišťuje, že složité hierarchické datové struktury – jako jsou struktury souborů, bezpečnostní parametry a parametry služeb – mohou být přenášeny a zpracovávány spolehlivě.

Architektura kódování BER-TLV je ze své podstaty hierarchická a samoopisná. Jeden datový objekt BER-TLV může při použití konstruovaného tagu zapouzdřit více podřízených TLV objektů ve svém poli Value. To umožňuje reprezentaci složitých, stromových datových struktur nezbytných pro mobilní telekomunikace, jako je adresářová struktura [EF](/mobilnisite/slovnik/ef/) (Elementary File) na USIM nebo uložení autentizačních vektorů a parametrů specifických pro síť. Přesná pravidla pro kódování tagu (včetně čísla tagu a třídy), kódování délky (krátká, dlouhá nebo neurčitá forma) a reprezentace hodnoty zajišťují, že jakákoli kompatibilní entita může dekódovat datový proud bez předchozí znalosti jeho obsahové struktury mimo definice specifikace. Tím se odděluje sémantika dat od přenosového formátu, což poskytuje značnou flexibilitu pro budoucí rozšíření a nové datové typy v ekosystému 3GPP.

Jeho role v síti je zásadní pro bezpečnou a spolehlivou správu identit účastníků a poskytování služeb. Pokaždé, když mobilní zařízení provádí autentizační proceduru se sítí, čte soubor z USIM nebo aktualizuje parametr služby, jsou data formátována pomocí BER-TLV. Robustnost tohoto kódování zabraňuje chybám při parsování, podporuje zpětnou i dopřednou kompatibilitu díky svému rozšiřitelnému prostoru tagů a umožňuje čipu UICC spravovat širokou škálu aplikací a dat standardizovaným způsobem. To dělá z BER-TLV kritickou, i když často neviditelnou, vrstvu protokolu, která zajišťuje integritu výměny dat na samém okraji mobilní sítě – v modulu identifikace účastníka.

## K čemu slouží

BER-TLV byl vytvořen k řešení problému efektivního a jednoznačného kódování strukturovaných dat pro přenos a ukládání v telekomunikačních systémech, zejména pro rozhraní čipových karet. Před přijetím takového standardizovaného kódování se používaly ad-hoc binární formáty, což vedlo k problémům s interoperabilitou, obtížím při parsování a výzvám při rozšiřování systémů o nové datové typy. Přijetí ASN.1 a jeho základních pravidel kódování poskytlo formální, mezinárodně standardizovanou metodu ([ITU-T](/mobilnisite/slovnik/itu-t/) X.690) pro popis a kódování datových struktur. 3GPP toto přijalo pro aplikace UICC, aby zajistilo, že všechna mobilní zařízení a síťová infrastruktura mohou spolehlivě komunikovat s moduly identifikace účastníka od jakéhokoli výrobce.

Historický kontext spočívá ve vývoji systémů GSM a 3G směrem ke složitějším službám vyžadujícím sofistikovanou správu dat na SIM kartě. Jak se služby posunuly od jednoduché identifikace účastníka k zahrnutí autentizačních algoritmů, souborových systémů a příkazů aplikačního nástrojového vybavení, stala se flexibilní a robustní reprezentace dat nezbytnou. BER-TLV řeší omezení pevných nebo proprietárních formátů kódování tím, že poskytuje samoopisný formát. Tag explicitně identifikuje datový objekt, pole délky umožňuje data proměnné velikosti a schopnost vnořování (konstruované kódování) umožňuje složité hierarchie. Tím byly vyřešeny kritické problémy s integritou dat, spolehlivostí parsování a budoucí rozšiřitelností bez nutnosti změn základního rozhraní příkazů mezi terminálem a kartou.

Jeho účel navíc spočívá v umožnění bezpečného a spravovatelného poskytování služeb. Standardizací kódování dat pro aplikace USIM/[ISIM](/mobilnisite/slovnik/isim/) zajistilo 3GPP, že citlivá bezpečnostní data, jako jsou kryptografické klíče a autentizační sekvence, mohou být zabalena a přenášena v předvídatelném, analyzovatelném formátu. To je zásadní pro prevenci chyb, které by mohly vést k bezpečnostním zranitelnostem nebo výpadkům služeb. Motivací bylo vytvořit základní, spolehlivou datovou vrstvu, která podporuje celý ekosystém mobilní identity účastníka, od základního přístupu k síti až po pokročilé služby IP Multimedia Subsystem (IMS), tím, že poskytuje společný jazyk pro data na čipu UICC.

## Klíčové vlastnosti

- Strukturované kódování tripletem (Tag, Length, Value) pro samoopisné datové objekty
- Podpora primitivních (jednoduchá data) i konstruovaných (vnořené TLV objekty) datových typů
- Kódování určité a neurčité délky pro zpracování datových náplní proměnné velikosti
- Hierarchická reprezentace dat umožňující složité, stromové struktury (např. adresáře souborů)
- Rozšiřitelný prostor tagů se čtyřmi třídami (Univerzální, Aplikační, Kontextově specifické, Privátní) pro budoucí kompatibilitu
- Standardizováno v 3GPP TS 31.102/31.103 pro datové struktury příkazů a odpovědí USIM/ISIM

## Definující specifikace

- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification

---

📖 **Anglický originál a plná specifikace:** [BER-TLV na 3GPP Explorer](https://3gpp-explorer.com/glossary/ber-tlv/)
