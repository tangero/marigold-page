---
slug: "aac-lc"
url: "/mobilnisite/slovnik/aac-lc/"
type: "slovnik"
title: "AAC-LC – Advanced Audio Coding-Low Complexity"
date: 2025-01-01
abbr: "AAC-LC"
fullName: "Advanced Audio Coding-Low Complexity"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aac-lc/"
summary: "AAC-LC je standardizovaný typ zvukového objektu s nízkou složitostí v rámci rodiny MPEG-4 Advanced Audio Coding (AAC), specifikovaný organizací 3GPP pro mobilní multimediální služby. Poskytuje vysoce"
---

AAC-LC je standardizovaný zvukový kodek s nízkou složitostí v rámci rodiny MPEG-4 AAC, specifikovaný organizací 3GPP pro vysoce kvalitní a účinnou zvukovou kompresi v mobilních multimediálních službách.

## Popis

Advanced Audio Coding-Low Complexity (AAC-LC) je specifický typ zvukového objektu definovaný v rámci standardu pro kódování zvuku MPEG-4 Part 3 ([ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 14496-3), který byl přijat a specifikován organizací 3GPP pro použití v mobilních komunikačních systémech. Jako zvukový kodek funguje tak, že analyzuje spektrální obsah zvukového signálu, aplikuje percepční modely k odstranění neslyšitelných složek (proces známý jako percepční kódování) a efektivně kvantuje a kóduje zbývající data. Označení 'Low Complexity' (nízká složitost) odkazuje na jeho specifický algoritmický profil, který je optimalizován tak, aby poskytoval vysokou zvukovou kvalitu při zachování výpočetní náročnosti vhodné pro implementaci na mobilních zařízeních s omezeným výkonem procesoru a životností baterie. Komprese je dosažena využitím maskovacích vlastností lidského sluchového systému a použitím technik transformačního kódování, typicky pomocí Modifikované diskrétní kosinové transformace ([MDCT](/mobilnisite/slovnik/mdct/)).

V rámci architektury 3GPP není AAC-LC síťový protokol, ale mediální kodek specifikovaný pro použití ve službách aplikační vrstvy. Jeho specifikace jsou obsaženy v 3GPP Technických specifikacích (TS) 26.401, která definuje obecné požadavky na zvukový kodek a rozhraní, a v TS 26.406, která poskytuje podrobné specifikace shody a testování pro AAC-LC. Samotný kodek funguje nezávisle na vrstvách rádiového přístupu nebo jádra sítě; je využíván multimediálními aplikacemi (např. přehrávačem médií nebo streamovacím klientem) ke kódování zvuku pro přenos nebo dekódování přijatého zvuku pro přehrávání. Jeho výkon je klíčový pro kvalitu uživatelského zážitku (QoE) služeb pro koncové uživatele, jako je Packet-Switched Streaming Service (PSS), Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a později Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) a multimediální telefonie.

Klíčové technické součásti fungování AAC-LC zahrnují jeho banku filtrů, percepční model, kvantizaci a moduly bezeztrátového kódování. Banka filtrů rozděluje zvukový signál do kmitočtových pásem, percepční model určuje prahy právě znatelného zkreslení (maskovací prahy) pro každé pásmo a kvantizace přiděluje bity podle toho. Pro další kompresi je pak aplikováno Huffmanovo kódování. Jeho úlohou v ekosystému 3GPP je poskytnout standardizovanou, interoperabilní a účinnou metodu pro doručování zvukového obsahu vysoké kvality přes rádiové spoje s omezenou přenosovou kapacitou. Specifikací AAC-LP organizace 3GPP zajišťuje, že zařízení a síťové prvky různých dodavatelů mohou spolehlivě kódovat a dekódovat zvukové streamy, což usnadňuje rozsáhlé nasazení služeb a konzistentní uživatelský zážitěk napříč zařízeními a operátory.

## K čemu slouží

AAC-LC byl zaveden pro uspokojení potřeby vysoce kvalitního a výpočetně efektivního zvukového kodeku pro mobilní multimediální služby v sítích 3G a později 4G. Před jeho standardizací mobilní zvukové služby často spoléhaly na jednodušší kodeky, jako je [AMR-NB](/mobilnisite/slovnik/amr-nb/) pro řeč, nebo formáty s nižší věrností pro hudbu, které byly nedostatečné pro poskytnutí přesvědčivého zážitku ze streamování hudby nebo videa se zvukem. Růst služeb mobilních dat a poptávka spotřebitelů po multimediálním obsahu vytvořily požadavek na zvukový kodek, který by mohl poskytovat kvalitu blízkou [CD](/mobilnisite/slovnik/cd/) při nižších přenosových rychlostech než nekomprimovaný PCM zvuk, a přitom byl proveditelný pro implementaci na energeticky citlivých procesorech prvních chytrých telefonů a feature phone.

Vytvoření AAC-LC v rámci 3GPP bylo motivováno snahou využít pokročilé kompresní schopnosti standardu MPEG-4 [AAC](/mobilnisite/slovnik/aac/), který již byl úspěšný v jiných doménách (jako je digitální rádio a online obchody s hudbou), a zároveň jej přizpůsobit mobilnímu prostředí. Profil 'Low Complexity' byl konkrétně vybrán k vyřešení problému vysokých výpočetních nákladů spojených s jinými profily AAC (jako je AAC Main Profile). Optimalizací algoritmu pro nižší zatížení procesoru a spotřebu paměti umožnil AAC-LC nasazení služeb zvuku vysoké kvality bez nadměrného vybíjení baterie nebo nutnosti neúměrně drahého hardwaru, čímž se pokročilé multimédium stalo masově rozšířenou funkcí v mobilních sítích.

## Klíčové vlastnosti

- Percepční zvukové kódování založené na standardu MPEG-4 AAC
- Optimalizováno pro nízkou výpočetní složitost a spotřebu paměti vhodnou pro mobilní zařízení
- Poskytuje vysokou zvukovou kvalitu při přenosových rychlostech od 48 kbit/s do 256 kbit/s na kanál
- Podporuje více vzorkovacích frekvencí (např. 8 kHz až 48 kHz) a kanálových konfigurací (mono, stereo)
- Používá banku filtrů založenou na Modifikované diskrétní kosinové transformaci (MDCT) pro účinnou spektrální analýzu
- Zahrnuje Huffmanovo kódování pro bezeztrátovou kompresi dat po kvantizaci

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.401** (Rel-19) — Enhanced aacPlus Audio Codec Mapping
- **TS 26.406** (Rel-19) — Enhanced aacPlus Audio Codec Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [AAC-LC na 3GPP Explorer](https://3gpp-explorer.com/glossary/aac-lc/)
