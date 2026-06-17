---
slug: "lbrm"
url: "/mobilnisite/slovnik/lbrm/"
type: "slovnik"
title: "LBRM – Limited Buffer Rate Matching"
date: 2025-01-01
abbr: "LBRM"
fullName: "Limited Buffer Rate Matching"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lbrm/"
summary: "Technika kanálového kódování a přizpůsobení přenosové rychlosti používaná primárně v 5G NR k efektivní adaptaci transportního bloku na přidělené fyzické zdroje při omezené velikosti softwarového vyrov"
---

LBRM je technika přizpůsobení přenosové rychlosti (rate matching) v 5G NR, která efektivně adaptuje transportní blok na přidělené fyzické zdroje, když je velikost softwarového vyrovnávacího paměti přijímače omezená.

## Popis

Limited Buffer Rate Matching (LBRM) je sofistikovaný proces fyzické vrstvy definovaný ve specifikacích 3GPP New Radio (NR) pro downlinkový sdílený kanál ([PDSCH](/mobilnisite/slovnik/pdsch/)) a uplinkový sdílený kanál (PUSCH). Je nedílnou součástí řetězce kanálového kódování, umístěnou mezi kodér Low-Density Parity-Check ([LDPC](/mobilnisite/slovnik/ldpc/)) a modulátor. Hlavní funkcí LBRM je provádět přizpůsobení přenosové rychlosti (rate matching) – proces vytváření kódového slova přesné délky potřebné pro přidělené časově-frekvenční zdroje – za specifického omezení, že přijímající uživatelské zařízení (UE) disponuje konečnou softwarovou vyrovnávací pamětí pro kanálové bity, určenou k ukládání logaritmických poměrů věrohodnosti (LLR) během kombinování v rámci Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)).

Princip fungování LBRM je zásadně svázán s HARQ operací. Při vysílání transportního bloku vytvoří LDPC kodér mateřské kódové slovo. Konvenční schéma přizpůsobení přenosové rychlosti s cirkulární pamětí by z tohoto mateřského kódového slova vybírala bity. Pokud je však velikost softwarového vyrovnávacího paměti UE menší než velikost celého mateřského kódového slova (což je běžné u UE s nižší složitostí), musí gNB omezit množinu bitů, které může potenciálně vysílat napříč všemi HARQ retransmisemi, pouze na ty, které je UE schopno uložit. LBRM tuto omezenou množinu definuje. Proces přizpůsobení přenosové rychlosti na straně gNB vybírá bity pouze z tohoto předdefinovaného, velikostí paměti omezeného okna uvnitř cirkulární paměti. Tím je zajištěno, že jakýkoli vyslaný bit, ať už v počáteční transmisi nebo retransmisi, může být UE uložen a kombinován.

Klíčové komponenty zahrnují konfiguraci omezené velikosti vyrovnávací paměti (Nref), která je odvozena od kategorie UE a její nahlášené schopnosti. gNB tuto informaci využívá k určení výstupu LBRM procesu přizpůsobení přenosové rychlosti. Tato technika hraje v síti klíčovou roli tím, že umožňuje efektivní podporu UE s výrazně odlišnými výpočetními schopnostmi a cenovými hladinami, od špičkových smartphonů po jednoduchá IoT zařízení, vše v rámci stejné NR nosné. Zajišťuje, že pokročilé zisky kanálového kódování LDPC jsou zachovány i pro UE s omezenou pamětí, čímž zabraňuje degradaci výkonu, která by nastala, pokud by gNB vysílal bity, které UE není schopno zpracovat.

## K čemu slouží

LBRM bylo zavedeno v 3GPP Release 14 pro studii proveditelnosti NR a ustáleno v pozdějších releasech za účelem řešení specifického problému vyplývajícího z nového schématu kanálového kódování 5G NR. NR přijalo [LDPC](/mobilnisite/slovnik/ldpc/) kódy pro datové kanály, které jsou výborné z hlediska výkonu, ale generují velmi velká mateřská kódová slova, zejména pro velké velikosti transportních bloků podporované 5G. Softwarová vyrovnávací paměť potřebná k uložení LLR pro celé mateřské kódové slovo napříč více [HARQ](/mobilnisite/slovnik/harq/) procesy by byla nepřiměřeně velká a nákladná, zvláště pro IoT zařízení s nízkou složitostí a nízkým příkonem.

Účelem LBRM je oddělit implementační náklady UE (určené velikostí softwarové vyrovnávací paměti) od výkonu systému v oblasti špičkové přenosové rychlosti. Bez LBRM by síť musela předpokládat, že všechna UE dokážou uložit celé kódové slovo, nebo by musela výrazně omezovat schémata kódování a modulace pro schopná UE. LBRM umožňuje gNB přesně vědět, kterou podmnožinu zakódovaných bitů může konkrétní UE uložit. To síti umožňuje plánovat vysílání s vysokou spektrální účinností pro pokročilá UE a zároveň podporovat nízkonákladová zařízení ve stejné síti, a to vše bez kompromisů v HARQ kombinačním zisku pro jakékoli zařízení. Řeší tak ekonomickou a praktickou nutnost diverzifikovaného ekosystému zařízení v 5G.

## Klíčové vlastnosti

- Umožňuje efektivní HARQ operaci pro UE s omezenou softwarovou vyrovnávací pamětí.
- Integruje se s NR LDPC kanálovým kódováním a přizpůsobením přenosové rychlosti s cirkulární pamětí.
- Závisí na schopnostech UE, přičemž omezená velikost vyrovnávací paměti Nref je signalizována UE.
- Zajišťuje, že gNB vysílá pouze bity, které mohou být uloženy ve vyrovnávací paměti cílového UE.
- Klíčové pro podporu širokého spektra složitosti a cenových hladin UE.
- Udržuje výkon spojení a kódový zisk i přes paměťová omezení.

## Související pojmy

- [LDPC – Low-Density Parity-Check](/mobilnisite/slovnik/ldpc/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)

## Definující specifikace

- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [LBRM na 3GPP Explorer](https://3gpp-explorer.com/glossary/lbrm/)
