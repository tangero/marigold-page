---
slug: "aei"
url: "/mobilnisite/slovnik/aei/"
type: "slovnik"
title: "AEI – Application Entity Invocation"
date: 2025-01-01
abbr: "AEI"
fullName: "Application Entity Invocation"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/aei/"
summary: "AEI je schopnost služby CAMEL (Customised Applications for Mobile network Enhanced Logic), která umožňuje dynamické vyvolání externí aplikační logiky během hovoru nebo relace. Umožňuje operátorům inte"
---

AEI je schopnost služby CAMEL, která umožňuje dynamické vyvolání externí aplikační entity (Application Entity) během hovoru nebo relace za účelem integrace vlastních síťových služeb.

## Popis

Vyvolání aplikační entity (Application Entity Invocation, AEI) je základní komponenta v architektuře 3GPP [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic), specifikovaná především v TS 29.078. Funguje jako schopnost služby, která usnadňuje interakci mezi funkcí řízení hovoru/relace jádra sítě a externí, operátorem definovanou aplikační entitou ([AE](/mobilnisite/slovnik/ae/)). AE je logický uzel, často součást bodu řízení služeb (SCP) nebo aplikačního serveru ([AS](/mobilnisite/slovnik/as/)), který hostuje vlastní logiku služby. Mechanismus vyvolání je řízen profilem CAMEL Subscription Information ([CSI](/mobilnisite/slovnik/csi/)) uloženým v [HLR](/mobilnisite/slovnik/hlr/)/[HSS](/mobilnisite/slovnik/hss/), který instruuje obsluhující síťový uzel (jako gsmSCF), aby navázal dialog s určenou AE na předdefinovaných detekčních bodech (DPs) v modelu stavu hovoru nebo relace.

Operačně, když účastník zahájí nebo přijme hovor/relaci, navštívená ústředna ([MSC](/mobilnisite/slovnik/msc/)) nebo funkce řízení relací ([CSCF](/mobilnisite/slovnik/cscf/)) zkontroluje aktivní spouštěče CAMEL. Pokud je přítomna CSI související s AEI, gsmSCF (nebo jeho ekvivalent) funguje jako CAMEL Service Environment (CSE) a zahájí transakci s externí AE. To zahrnuje odeslání operace initial DP (IDP) obsahující podrobnosti o hovoru a data účastníka. AE poté provede svou servisní logiku – což může zahrnovat dotazování databáze, aplikaci pravidel účtování nebo úpravu rozhodnutí o směrování – a vrátí instrukce gsmSCF. Tyto instrukce, předávané prostřednictvím operací CAMEL Application Part (CAP), jako jsou Continue, Connect nebo ApplyCharging, řídí jádro sítě v tom, jak pokračovat v obsluze hovoru.

Architektura spoléhá na standardizovaný protokol CAMEL Application Part (CAP), rozšíření SS7/INAP, pro signalizaci mezi gsmSCF a AE. AEI není služba sama o sobě, ale obecný rámec pro vyvolání, který umožňuje služby jako předplacené účtování, kontrola podvodů, služby VPN a lokalizační směrování. Jeho návrh odděluje servisní logiku od základního zpracování hovoru, což umožňuje rychlé nasazení a přizpůsobení služeb bez nutnosti úpravy každé ústředny v síti. Schopnost AEI je nedílnou součástí konceptu Inteligentní sítě (IN) v rámci systémů 3GPP a poskytuje standardizovanou, na dodavateli nezávislou metodu pro operátory k vytváření a správě přidaných služeb.

## K čemu slouží

AEI bylo vytvořeno, aby řešilo potřebu flexibilního vytváření a nasazování služeb specifických pro operátora v mobilních sítích, což znamenalo posun od pevných, do ústředen vestavěných funkcí raných systémů. Před zavedením CAMEL a schopností jako AEI vyžadovalo zavádění nových služeb proprietární úpravy ústředen od každého dodavatele, což bylo pomalé, nákladné a bránilo interoperabilitě. Paradigma Inteligentní sítě (IN), které CAMEL implementuje pro GSM a později systémy 3GPP, mělo za cíl oddělit servisní logiku od základních přepojovacích funkcí. AEI poskytuje konkrétní mechanismus pro 'vyvolání' této externí logiky, čímž řeší problém, jak dynamicky spouštět vlastní aplikace během hovoru nebo datové relace na základě profilů účastníků a událostí v reálném čase.

Historicky, jak se mobilní sítě vyvíjely a rostla konkurence, operátoři požadovali schopnost rychle nasazovat diferencované služby, jako je předplacené účtování, virtuální privátní sítě pro firmy a inteligentní směrování hovorů. AEI jako součást rámce CAMEL zavedeného ve 3GPP Release 8 a dříve tento proces vyvolání standardizovalo. Vyřešilo omezení monolitických síťových architektur definováním jasného, protokolem založeného rozhraní (CAP) mezi řízením hovoru sítě a externími aplikačními servery. To umožnilo operátorům vyvíjet nebo pořizovat služby nezávisle na dodavatelích jejich síťové infrastruktury, což podpořilo inovace a zkrátilo dobu uvedení nových, výnos generujících funkcí na trh.

## Klíčové vlastnosti

- Dynamické spouštění externí aplikační logiky na základě detekčních bodů (DPs) CAMEL
- Používá standardizovaný protokol CAMEL Application Part (CAP) pro signalizaci
- Umožněno informací o předplatném CAMEL (CSI) uloženou v HLR/HSS
- Podporuje širokou škálu služeb včetně předplaceného účtování, VPN a inteligentního směrování
- Odděluje servisní logiku od přepojovacích funkcí jádra sítě
- Poskytuje rámec pro vytváření a nasazování služeb nezávislý na dodavateli

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)
- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)

## Definující specifikace

- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification

---

📖 **Anglický originál a plná specifikace:** [AEI na 3GPP Explorer](https://3gpp-explorer.com/glossary/aei/)
