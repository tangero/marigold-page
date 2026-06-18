---
slug: "xhtml"
url: "/mobilnisite/slovnik/xhtml/"
type: "slovnik"
title: "XHTML – Extensible HyperText Markup Language"
date: 2025-01-01
abbr: "XHTML"
fullName: "Extensible HyperText Markup Language"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/xhtml/"
summary: "Značkovací jazyk standardizovaný pro použití v sítích 3GPP k formátování a zobrazování webového obsahu na mobilních zařízeních. Umožňuje bohaté multimediální zprávy (MMS) a mobilní webové prohlížení a"
---

XHTML je značkovací jazyk standardizovaný pro použití v sítích 3GPP k formátování a zobrazování webového obsahu na mobilních zařízeních, který umožňuje služby jako MMS a mobilní prohlížení pro konzistentní uživatelský zážitek.

## Popis

XHTML (Extensible HyperText Markup Language) je značkovací jazyk založený na [XML](/mobilnisite/slovnik/xml/), který kombinuje známou syntaxi [HTML](/mobilnisite/slovnik/html/) s přísnými syntaktickými pravidly XML. V rámci ekosystému 3GPP je formálně definován v TS 26.953 jako klíčová komponenta pro formátování obsahu, zejména pro službu Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)). Tento jazyk strukturová obsah, jako je text, obrázky a instrukce pro rozložení, do dobře formovaného dokumentu, který může být spolehlivě parsován a vykreslen mobilním uživatelským zařízením (UE). Architektura XHTML dokumentu pro MMS zahrnuje hlavičkovou sekci (head) s metadaty a tělo dokumentu (body) obsahující vlastní obsahové elementy, přičemž vše dodržuje definovanou Document Type Definition ([DTD](/mobilnisite/slovnik/dtd/)).

Během provozu, když je MMS vytvořena nebo přijata, XHTML dokument funguje jako prezentační vrstva. Klient pro zasílání zpráv nebo prohlížeč na UE interpretuje XHTML tagy, aby zobrazil formátovaný text, vložil obrázky a aplikoval základní styly. Tento proces zahrnuje parsování XML struktury, validaci vůči specifikované DTD (např. XHTML Mobile Profile) a následné vykreslení na obrazovce zařízení. Specifikace 3GPP zajišťují podporu základní sady XHTML modulů, což garantuje minimální úroveň interoperability mezi telefony různých výrobců a síťovými elementy, jako je Multimedia Messaging Service Center (MMSC).

Jeho role v síti je primárně ve vrstvě služeb, odděluje tvorbu obsahu od vykreslovacích enginů specifických pro dané zařízení. Poskytnutím standardizovaného formátu umožňuje poskytovatelům obsahu a síťovým operátorům vytvářet bohaté zprávy a základní webové stránky, které jsou přenositelné. Tato standardizace byla klíčová pro komerční úspěch MMS, neboť zabránila fragmentaci a zajistila, že zpráva odeslaná ze sítě jednoho operátora na zařízení v síti jiného operátora bude zobrazena podle očekávání. I když jeho význam poklesl s nástupem nativních aplikací a plnohodnotných prohlížečů s HTML5, XHTML-MP představoval kritický krok ve vývoji mobilních datových služeb.

## K čemu slouží

XHTML byl zaveden, aby vyřešil problém nekonzistentního zobrazování obsahu na raných mobilních zařízeních, což narušovalo uživatelský zážitek u datových služeb jako [MMS](/mobilnisite/slovnik/mms/) a mobilní internet. Před jeho standardizací byly formáty obsahu často proprietární nebo založené na zjednodušeném [HTML](/mobilnisite/slovnik/html/), což vedlo k rozbitému rozložení, chybějícím obrázkům a špatnému celkovému dojmu při přenosu obsahu přes hranice sítí nebo zařízení. Motivací bylo vytvořit jednotný standard založený na [XML](/mobilnisite/slovnik/xml/), který by mohl být spolehlivě zpracován tehdejšími prohlížeči a klienty pro zasílání zpráv s omezenými možnostmi.

Historický kontext představovalo zavedení paketově spínaných sítí ([GPRS](/mobilnisite/slovnik/gprs/), EDGE) a spuštění MMS jako nástupce SMS. Aby se MMS stala atraktivní službou s formátováním textu a vloženými obrázky, byl potřebný robustní prezentační jazyk. XHTML, konkrétně podmnožina Mobile Profile, byl zvolen proto, že nabízel přísnější syntaxi než HTML, což usnadňovalo parsování na zařízeních s omezenými zdroji, a zároveň poskytoval dostatečnou výrazovou sílu pro bohaté zprávy. Odstranil omezení jazyka Wireless Markup Language (WML) tím, že nabídl větší flexibilitu a vývojový model bližší mainstreamovému webu.

Jeho přijetí navíc podpořilo širší cíl 3GPP umožnit interoperabilní, na výrobci nezávislé služby. Specifikací XHTML v TS 26.953 poskytlo 3GPP stabilní cíl pro výrobce telefonů a vývojáře obsahu, což podpořilo ekosystém, ve kterém mohly být služby nasazovány ve velkém měřítku. To bylo nezbytné pro vybudování důvěry spotřebitelů a podniků v mobilní data přesahující hlas a jednoduchý text.

## Klíčové vlastnosti

- Přísná syntaxe založená na XML zajišťující spolehlivé parsování
- Definovaná podmnožina (XHTML Mobile Profile) pro zařízení s omezenými zdroji
- Podpora základního formátování textu a vkládání obrázků
- Oddělení struktury a prezentace pomocí podpory CSS
- Standardizovaná Document Type Definition (DTD) pro validaci
- Interoperabilita mezi různými UE a síťovými elementy

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [WAP – Wireless Application Protocol](/mobilnisite/slovnik/wap/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [XHTML na 3GPP Explorer](https://3gpp-explorer.com/glossary/xhtml/)
