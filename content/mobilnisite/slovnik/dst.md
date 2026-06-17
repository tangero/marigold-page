---
slug: "dst"
url: "/mobilnisite/slovnik/dst/"
type: "slovnik"
title: "DST – Discrete Sine Transform"
date: 2025-01-01
abbr: "DST"
fullName: "Discrete Sine Transform"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dst/"
summary: "Diskrétní sinusová transformace (DST) je matematická transformace používaná v audiokodecích a řečových kodecích 3GPP pro kompresi a zpracování signálu. Převádí konečnou posloupnost datových bodů na re"
---

DST je matematická transformace používaná v audiokodecích a řečových kodecích 3GPP, která převádí posloupnost datových bodů na složky sinusových vln pro účinnou kompresi a zpracování signálu.

## Popis

Diskrétní sinusová transformace (DST) je transformace příbuzná Fourierově transformaci, podobná diskrétní kosinové transformaci ([DCT](/mobilnisite/slovnik/dct/)), ale jako bázi používá pouze sinusové funkce. Ve specifikacích 3GPP, zejména pro audiokodeky a řečové kodeky, se DST používá jako nástroj pro analýzu a kompresi signálu. Pracuje s konečnou diskrétní posloupností reálných čísel a transformuje je z časové (nebo prostorové) domény do frekvenční reprezentace složené z vážených sinusových funkcí. Tato reprezentace je pro určité typy signálů často kompaktnější, což umožňuje účinnou kompresi tím, že se odstraní nebo kvantují transformační koeficienty, které málo přispívají k vnímané kvalitě signálu.

V kodeku, jako je kodek Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) specifikovaný v 3GPP TS 26.906, se DST aplikuje jako součást modulu transformačního kódování pro zpracování audiostop. Proces zahrnuje okénkování segmentu audio signálu, aplikaci DST na okénkované vzorky za účelem získání sady transformačních koeficientů a následné kvantování a kódování těchto koeficientů pro přenos. Na straně dekodéru se aplikuje inverzní DST k rekonstrukci audio signálu v časové oblasti z přijatých koeficientů. Volba DST oproti DCT nebo jiným transformacím je založena na jejích spektrálních vlastnostech a výkonu se specifickými statistickými charakteristikami kódovaného signálu, jako jsou určité typy reziduálních signálů po lineární predikci.

Role DST v síti 3GPP je integrována do funkcí zpracování médií v uživatelském zařízení (UE) a síťových uzlech, jako je Media Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)). Jedná se o klíčovou algoritmickou složku, která umožňuje vysoce kvalitní audio kódování s nízkým datovým tokem, což je nezbytné pro efektivní využití zdrojů rádiové a přenosové sítě. Poskytnutím kompaktní spektrální reprezentace DST přímo přispívá k kompresní účinnosti kodeku, což ovlivňuje celkovou kvalitu uživatelského zážitku u hlasových a audio služeb v celulárních sítích. Její implementace je optimalizována pro nízkou výpočetní složitost, aby vyhověla procesním omezením mobilních zařízení.

## K čemu slouží

Diskrétní sinusová transformace byla do specifikací audiokodeků 3GPP zařazena za účelem zlepšení kompresní účinnosti a audio kvality pro multimediální služby. Řeší základní problém reprezentace audio signálů ve formě, která umožňuje výraznou redukci dat bez podstatné percepční ztráty. Motivace pro použití DST, vedle nebo místo jiných transformací jako je [DCT](/mobilnisite/slovnik/dct/), vychází z jejích matematických vlastností, které mohou být vhodnější pro dekorrelaci určitých typů audio signálů, zejména predikčních reziduí, což vede k účinnějšímu kódování.

Před přijetím pokročilých technik transformačního kódování se kodeky více spoléhaly na jednodušší vlnové kódování nebo parametrické modely, které měly omezení v průzračnosti nebo efektivitě šířky pásma. Zařazení DST do kodeků jako je [EVS](/mobilnisite/slovnik/evs/) bylo hnací silou neustálého úsilí o dosažení vyšší kvality při nižších datových tocích, zejména pro hudbu a smíšený obsah ve hlasových hovorech. Řešila problém, jak kompaktně reprezentovat spektrální obálku audio signálu poté, co dominantní predikovatelné složky (jako je výška tónu a formanty) byly odstraněny v předchozích stupních kodeku.

Historický kontext představuje vývoj od úzkopásmové telefonní řeči k vysokokvalitnímu hlasu a plnopásmovým audio službám v celulárních sítích. S rostoucími uživatelskými nároky potřebovaly kodeky sofistikovanější nástroje. DST, jakožto dobře známý nástroj zpracování signálu z literatury o kompresi obrazu a zvuku, byla vybrána a optimalizována pro prostředí mobilní komunikace s reálným časem a omezenými zdroji. Jejím účelem je umožnit úspory datového toku nezbytné pro kapacitu sítě při zachování nebo zlepšení vnímané audio věrnosti.

## Klíčové vlastnosti

- Transformace příbuzná Fourierově transformaci využívající sinusové bázové funkce
- Používá se pro převod z časové do frekvenční domény v audiokodecích
- Poskytuje kompaktní spektrální reprezentaci pro účinnou kompresi
- Implementována v kodecích jako EVS pro transformační kódování audiostop
- Podporuje inverzní transformaci pro dokonalou rekonstrukci (v bezztrátovém případě)
- Optimalizována pro nízkou výpočetní složitost vhodnou pro mobilní zařízení

## Související pojmy

- [MDCT – Modified Discrete Cosine Transform](/mobilnisite/slovnik/mdct/)

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [DST na 3GPP Explorer](https://3gpp-explorer.com/glossary/dst/)
