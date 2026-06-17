---
slug: "hrir"
url: "/mobilnisite/slovnik/hrir/"
type: "slovnik"
title: "HRIR – Head-Related Room Impulse Response"
date: 2025-01-01
abbr: "HRIR"
fullName: "Head-Related Room Impulse Response"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hrir/"
summary: "Datový model pro prostorové zvukové vykreslování (rendering) ve službách rozšířené reality (XR) a imerzivních médií. Kombinuje funkce přenosu závislé na hlavě (HRTF) s akustikou místnosti, aby simulov"
---

HRIR je datový model 3GPP, který kombinuje funkce přenosu závislé na hlavě (Head-Related Transfer Functions) s akustikou místnosti za účelem simulace realistického 3D zvuku z konkrétních bodů ve virtuálním prostoru pro služby XR v sítích 5G.

## Popis

Head-Related Room Impulse Response (HRIR) je standardizovaný datový model definovaný 3GPP pro reprezentaci prostorových zvukových scén. Je klíčovou součástí architektur 5G Media Streaming ([5GMS](/mobilnisite/slovnik/5gms/)) a 5G Immersive Media (5GIM), které umožňují doručování imerzivních zvukových zážitků, jako je video 360°, virtuální realita (VR) a rozšířená realita ([AR](/mobilnisite/slovnik/ar/)). Technicky je HRIR sada binaurálních impulsních odezev, které matematicky popisují akustickou cestu od zdroje zvuku ve virtuálním prostředí k levému a pravému bubínku posluchače. Tato cesta zahrnuje směrové filtrační efekty způsobené hlavou, trupem a ušními boltci (pinnae) posluchače – známé jako funkce přenosu závislé na hlavě ([HRTF](/mobilnisite/slovnik/hrtf/)) – v kombinaci s dozvukem a akustickými charakteristikami virtuální místnosti nebo prostředí. Model umožňuje parametrizaci pozice zdroje, vlastností místnosti a orientace posluchače.

V síťové architektuře jsou data HRIR typicky generována tvůrci obsahu nebo specializovanými servery pro zpracování zvuku. Tato data mohou být streamována jako metadata spolu s audiovizuálním obsahem nebo stažena do zařízení uživatele (např. headsetu XR nebo smartphonu). Mediální přehrávač nebo zvukový renderer na straně klienta pak data HRIR využívá v reálném čase ke konvoluci monofonních nebo objektově založených zvukových proudů, čímž vytváří binaurální zvukový signál, který je přehráván přes sluchátka. Tento proces konvoluce aplikuje směrové a místnostní akustické stopy na zvuk, čímž klame lidský sluchový systém, aby vnímal zvuk jako přicházející z konkrétních míst v trojrozměrném prostoru kolem posluchače.

Standardizace HRIR ve specifikacích 3GPP (jako je TS 26.118 pro 5G Media Streaming a TS 26.254 pro Immersive Media) zajišťuje interoperabilitu mezi obsahovými servery, sítěmi 5G a koncovými uživatelskými zařízeními. Definuje formáty pro reprezentaci, ukládání a přenos dat HRIR, což umožňuje efektivní doručování přes bezdrátové spoje s omezenou přenosovou kapacitou. Model podporuje dynamické aktualizace, což umožňuje interaktivní zážitky, kde se mohou měnit zvukové zdroje nebo perspektiva posluchače. Tím, že poskytuje společný jazyk pro prostorový zvuk, HRIR usnadňuje vytvoření škálovatelného ekosystému pro služby imerzivních médií, což je klíčový případ užití a hnací síla příjmů pro sítě 5G a budoucí generace.

## K čemu slouží

HRIR byl vytvořen, aby vyřešil nedostatek standardizovaných, síťově efektivních metod pro doručování kvalitního prostorového zvuku v aplikacích imerzivních médií přes mobilní sítě. Před jeho standardizací byla řešení pro imerzivní zvuk často proprietární, specifická pro dané zařízení, nebo vyžadovala přenos více samostatných zvukových kanálů (např. surround sound 5.1 nebo 7.1), což je pro streamování neefektivní a neposkytuje skutečný 3D zvuk pro zážitky s sledováním polohy hlavy, jako je VR. Vzestup rozšířené reality (XR) jako primárního případu užití 5G vytvořil naléhavou potřebu po lehkém, parametrickém zvukovém popisu, který by umožnil přesvědčivé 3D zvukové scenérie bez neúměrné spotřeby přenosové kapacity.

Motivace vychází ze zásadní role, kterou zvuk hraje v imerzi. Samotná vizuální imerze není pro přesvědčivé virtuální zážitky dostačující; prostorový zvuk, který se dynamicky mění s pohybem hlavy uživatele, je klíčový pro pocit přítomnosti a realismus. HRIR to řeší tím, že poskytuje kompaktní datový model popisující akustickou scénu, což umožňuje provádět výpočetně náročné zvukové vykreslování (konvoluci) na výkonném uživatelském zařízení. To je v souladu s paradigmatem edge computingu v 5G, kde je náročné zpracování přesunuto ze sítě na zařízení. Standardizace tohoto modelu zajišťuje, že obsah vytvořený jednou může být správně vykreslen na jakémkoli kompatibilním zařízení, což podporuje široký ekosystém pro imerzivní média a umožňuje poskytovatelům služeb nabízet konzistentní, kvalitní zvukové zážitky jako součást jejich portfolia služeb 5G.

## Klíčové vlastnosti

- Parametrická reprezentace binaurálních impulsních odezev místnosti
- Podpora dynamického umísťování zdrojů a orientace posluchače
- Umožňuje efektivní streamování přes sítě 5G přenosem kompaktních metadat namísto vícekanálového zvuku
- Integruje se s architekturami 5G Media Streaming (5GMS) a doručování imerzivních médií
- Usnadňuje interoperabilitu mezi nástroji pro tvorbu obsahu, sítěmi a přehrávacími zařízeními
- Umožňuje realistické 3D zvukové vykreslování pro zážitky VR, AR a videa 360°

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.254** (Rel-19) — IVAS Rendering Functions Specification
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming

---

📖 **Anglický originál a plná specifikace:** [HRIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/hrir/)
