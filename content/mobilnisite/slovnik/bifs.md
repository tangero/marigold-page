---
slug: "bifs"
url: "/mobilnisite/slovnik/bifs/"
type: "slovnik"
title: "BIFS – Binary Format for Scenes"
date: 2025-01-01
abbr: "BIFS"
fullName: "Binary Format for Scenes"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bifs/"
summary: "BIFS je binární formát pro popis scény standardizovaný konsorciem 3GPP pro reprezentaci multimediálních prezentací v mobilním prostředí. Umožňuje efektivní přenos a vykreslování bohatého multimediální"
---

BIFS je binární formát pro popis scény standardizovaný konsorciem 3GPP pro efektivní přenos a vykreslování interaktivních multimediálních prezentací, včetně 2D/3D grafiky, audia a videa, přes mobilní sítě.

## Popis

BIFS (Binary Format for Scenes) je komplexní technologie pro popis scény standardizovaná konsorciem 3GPP jako součást multimediálního rámce MPEG-4. Slouží jako binární kódovací formát pro reprezentaci složitých multimediálních scén, které mohou zahrnovat 2D a 3D grafiku, audio proudy, video obsah, text a interaktivní prvky. Formát je speciálně navržen pro efektivní přenos přes mobilní sítě s omezenou šířkou pásma při zachování bohatých prezentačních schopností. Scény BIFS jsou komponovány jako hierarchické struktury uzlů, které definují prostorové a časové vztahy mezi různými mediálními objekty, což umožňuje synchronizované přehrávání a interakci uživatele.

V jádru BIFS pracuje na modelu scénového grafu, kde uzly reprezentují různé typy mediálních objektů a jejich vlastnosti. Scénový graf je organizován jako stromová struktura s nadřazenými a podřazenými vztahy definujícími prostorové transformace, vizuální vlastnosti a časové chování. BIFS podporuje dvě základní operace: popis scény (definice počátečního stavu prezentace) a aktualizace scény (dynamická modifikace scény během přehrávání). Binární kódování využívá efektivní kompresní techniky pro reprezentaci informací o scéně, včetně prediktivního kódování pro animační data a kvantizace pro numerické hodnoty. Tato binární reprezentace je výrazně kompaktnější než ekvivalentní textové formáty jako VRML nebo [XML](/mobilnisite/slovnik/xml/).

Architektura BIFS zahrnuje několik klíčových komponent: proud BIFS-Command pro aktualizace scény, proud BIFS-Anim pro animační data a rámec Object Descriptor pro správu mediálních zdrojů. Formát podporuje rozsáhlé 2D schopnosti prostřednictvím uzlů pro tvary, text, obrázky a vektorovou grafiku, zatímco 3D funkcionalita zahrnuje geometrické primitivy, transformace, osvětlení a materiály. Audio schopnosti zahrnují prostorové umístění zvuku a mixování více zvukových zdrojů. Interaktivní funkce jsou implementovány prostřednictvím senzorových uzlů reagujících na vstup uživatele, směrovacích uzlů pro šíření událostí a interpolačních uzlů pro řízení animace. BIFS také zahrnuje pokročilé funkce jako progresivní přenos, kde scény mohou být vykreslovány přírůstkově s příchodem dat, a selektivní aktualizace, které modifikují pouze konkrétní části scény.

V ekosystému 3GPP je BIFS integrován s dalšími komponentami MPEG-4 prostřednictvím specifikace MPEG-4 Systems. Spolupracuje s formátem souborů MPEG-4 ([ISO](/mobilnisite/slovnik/iso/) Base Media File Format) pro ukládání a s MPEG-4 Delivery Multimedia Integration Framework (DMIF) pro streamování. Formát podporuje synchronizaci mezi různými mediálními proudy prostřednictvím MPEG-4 Sync Layer a mechanismů Object Clock Reference. Scény BIFS mohou odkazovat na externí mediální objekty kódované různými MPEG-4 kodeky (jako H.264/[AVC](/mobilnisite/slovnik/avc/) pro video a [AAC](/mobilnisite/slovnik/aac/) pro audio) prostřednictvím Object Descriptorů, které poskytují přístupové informace a dekódovací parametry. Tato technologie umožňuje vytváření bohatých multimediálních aplikací včetně interaktivních prezentací, vzdělávacího obsahu, mobilních her a vylepšených služeb zasílání zpráv.

## K čemu slouží

BIFS byl vytvořen k řešení specifických výzev spojených s poskytováním bohatého multimediálního obsahu přes mobilní sítě s omezenou šířkou pásma a schopnostmi zařízení. Před jeho vývojem multimediální formáty pro popis scény jako VRML (Virtual Reality Modeling Language) používaly textové reprezentace, které byly pro přenos přes bezdrátové sítě neefektivní. Tyto formáty generovaly velké velikosti souborů, které spotřebovávaly nadměrnou šířku pásma a trpěly pomalým parsováním a vykreslováním na mobilních zařízeních s omezeným výpočetním výkonem. Mobilní průmysl potřeboval efektivnější řešení, které by mohlo poskytovat působivé multimediální zážitky při respektování omezení raných 3G sítí a mobilních telefonů.

Primární motivací pro BIFS bylo umožnit pokročilé multimediální služby v rodícím se 3G mobilním ekosystému. Když mobilní operátoři nasazovali paketové sítě schopné poskytovat datové služby, rostla poptávka po bohatých mediálních aplikacích přesahujících jednoduché prohlížení webu a email. Poskytovatelé obsahu chtěli vytvářet interaktivní prezentace, mobilní hry, vzdělávací materiály a vylepšené služby zasílání zpráv kombinující více typů médií. BIFS poskytl technický základ pro tyto služby tím, že nabídl binární formát, který byl zároveň kompaktní (snižující náklady na přenos a latenci) a bohatý na funkce (podporující interaktivitu, animaci a prostorové vztahy mezi mediálními objekty).

Dalším klíčovým problémem, který BIFS řešil, byla integrace různých typů médií v rámci jednotného rámce. Před MPEG-4 a BIFS multimediální systémy často používaly oddělené technologie pro různé mediální komponenty – jeden formát pro video, jiný pro audio a další pro grafiku. Tato fragmentace ztěžovala vytváření synchronizovaných, interaktivních prezentací. BIFS poskytl komplexní jazyk pro popis scény, který mohl orchestrovat všechny mediální prvky v rámci jediného rámce, s přesnou časovou kontrolou a prostorovým umístěním. Formát také řešil potřebu dynamických aktualizací scény, umožňující změnu obsahu v reakci na interakci uživatele nebo externí události bez nutnosti kompletního přenosu popisu scény.

## Klíčové vlastnosti

- Binární kódování pro efektivní přenos přes mobilní sítě
- Hierarchický model scénového grafu podporující 2D a 3D grafiku
- Dynamické aktualizace scény prostřednictvím proudů BIFS-Command a BIFS-Anim
- Integrace s MPEG-4 mediálními kodeky prostřednictvím Object Descriptorů
- Interaktivní schopnosti prostřednictvím senzorových uzlů a směrování událostí
- Mechanismy progresivního přenosu a selektivní aktualizace

## Definující specifikace

- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification

---

📖 **Anglický originál a plná specifikace:** [BIFS na 3GPP Explorer](https://3gpp-explorer.com/glossary/bifs/)
