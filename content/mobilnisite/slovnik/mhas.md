---
slug: "mhas"
url: "/mobilnisite/slovnik/mhas/"
type: "slovnik"
title: "MHAS – MPEG-H Audio Stream"
date: 2025-01-01
abbr: "MHAS"
fullName: "MPEG-H Audio Stream"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mhas/"
summary: "Standardizovaný formát bitového toku pro imerzivní a interaktivní audio založený na standardu MPEG-H 3D Audio. Umožňuje pokročilé audiozážitky, jako je objektové audio, personalizované míchání a dynam"
---

MHAS je standardizovaný formát bitového toku pro imerzivní a interaktivní audio, který umožňuje objektové audio, personalizované míchání a dynamickou adaptaci na různé systémy pro přehrávání.

## Popis

MPEG-H Audio Stream (MHAS) je normativní formát bitového toku a transportní mechanismus definovaný 3GPP pro doručování obsahu MPEG-H 3D Audio. MPEG-H Audio je pokročilý systém kódování audia, který v jediném bitovém toku podporuje kanálovou, objektovou a scénovou (Higher Order Ambisonics) reprezentaci audia. Formát MHAS je kontejner používaný pro paketizaci a transport těchto audio komponent. Technicky je tok MHAS složen z posloupnosti paketů MHAS. Každý paket obsahuje hlavičku se synchronizačními informacemi, typem paketu a informací o délce, následovanou datovou částí (payload). Datová část může nést různé typy jednotek audio dat, jako jsou konfigurační data MPEG-H Audio, snímky MPEG-H Audio nebo jiná pomocná data. Klíčovým provozním aspektem je jeho schopnost vrstvení a multiplexování. Více audio podtoků (např. hlavní audio program, popisný zvuk nebo jednotlivé audio objekty) může být multiplexováno do jediného toku MHAS. To umožňuje přijímači dekódovat pouze potřebné komponenty, což zpřístupňuje funkce jako personalizované audio, kde uživatel může zesílit hlas komentátora nebo zvolit preferovaný jazykový stopu. Tok MHAS je typicky přenášen uvnitř transportního kontejneru vyšší úrovně, jako je [MPEG-2](/mobilnisite/slovnik/mpeg-2/) Transport Stream (TS) pro vysílání nebo [ISO](/mobilnisite/slovnik/iso/) Base Media File Format ([ISOBMFF](/mobilnisite/slovnik/isobmff/)) pro streamování. V kontextu 5G Media Streaming ([5GMS](/mobilnisite/slovnik/5gms/)) by byl tok MHAS zabalen do segmentů [DASH](/mobilnisite/slovnik/dash/) nebo chunků [HLS](/mobilnisite/slovnik/hls/). Proces dekódování zahrnuje demultiplexování toku MHAS, extrakci příslušných snímků MPEG-H Audio a jejich dekódování pomocí dekodéru MPEG-H Audio. Dekodér následně vykresluje audio na základě přijatých metadat a možností systému pro přehrávání, který může sahat od stereofonních sluchátek po plný 22.2 kanálový domácí kinosystém. MHAS poskytuje flexibilní, do budoucna připravený audio formát, který dokáže přizpůsobit audio prezentaci v reálném čase posluchačovu prostředí a preferencím.

## K čemu slouží

MHAS byl zaveden, aby řešil omezení tradičních audiokodeků vzhledem k vyvíjejícím se spotřebitelským očekáváním a novým multimediálním formátům. Předchozí audio standardy, jako je Advanced Audio Coding ([AAC](/mobilnisite/slovnik/aac/)), byly primárně navrženy pro kanálové stereo nebo surround sound, nabízející pevné míchání. Vzestup videa Ultra High Definition ([UHD](/mobilnisite/slovnik/uhd/)), virtuální reality (VR) a interaktivních médií si vyžádal audio, které je stejně tak imerzivní, přizpůsobitelné a interaktivní. MPEG-H Audio, a tím pádem i MHAS, byl vytvořen jako jednotné řešení pro audio služby nové generace. Řeší problém doručení jediného audio bitového toku, který může být optimálně vykreslen na široké škále přehrávacích zařízení, od chytrých telefonů po sofistikované domácí kina, aniž by vyžadoval více paralelních audio stop. Také umožňuje inovace vysílatelů a poskytovatelů služeb prostřednictvím funkcí jako personalizované zesílení dialogů, přístupné audio popisy a interaktivní audio objekty, které může uživatel ovládat. Integrace MHAS do standardů 3GPP, počínaje Release 15, byla motivována posunem průmyslu směrem ke službám rozšířeného mobilního širokopásmového přístupu (eMBB) a médiím umožněným 5G. Vysoká šířka pásma a nízká latence 5G jsou ideální pro doručování bohatých, imerzivních mediálních zážitků a MHAS poskytuje standardizovanou audio komponentu, která doplňuje mediální zásobník nové generace vedle video standardů jako HEVC a VVC.

## Klíčové vlastnosti

- Podporuje multiplexování kanálových, objektových a Higher Order Ambisonics (HOA) audio komponent v jediném toku
- Umožňuje objektové audio pro interaktivní uživatelské zážitky (např. zesílení hlasu komentátora)
- Poskytuje metadata pro dynamické vykreslování k přizpůsobení audio výstupu konkrétním systémům pro přehrávání (od mono po 22.2 kanálů)
- Definuje paketovaný formát toku (MHAS) pro robustní transport přes vysílací nebo paketové sítě
- Umožňuje personalizované audio služby a funkce přístupnosti, jako je audio popis
- Standardizovaná integrace s formáty pro doručování médií, jako je MPEG-2 TS a DASH/ISOBMFF pro streamování

## Související pojmy

- [5GMS – 5G Media Streaming](/mobilnisite/slovnik/5gms/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [ISOBMFF – International Organization for Standards, Base Media File Format](/mobilnisite/slovnik/isobmff/)

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats

---

📖 **Anglický originál a plná specifikace:** [MHAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mhas/)
