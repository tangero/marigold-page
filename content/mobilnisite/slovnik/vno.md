---
slug: "vno"
url: "/mobilnisite/slovnik/vno/"
type: "slovnik"
title: "VNO – Virtual Network Operator"
date: 2025-01-01
abbr: "VNO"
fullName: "Virtual Network Operator"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/vno/"
summary: "Virtuální síťový operátor (VNO) je poskytovatel služeb, který nabízí telekomunikační služby koncovým uživatelům, ale nevlastní podkladovou infrastrukturu rádiového přístupu ani jádra sítě. Místo toho"
---

VNO je poskytovatel služeb, který nabízí telekomunikační služby bez vlastní síťové infrastruktury, místo toho si pronajímá kapacitu od mobilního síťového operátora.

## Popis

Virtuální síťový operátor (VNO), v mobilním kontextu také známý jako mobilní virtuální síťový operátor ([MVNO](/mobilnisite/slovnik/mvno/)), je obchodní subjekt, který poskytuje služby mobilní sítě své vlastní zákaznické základně, aniž by vlastnil licencované rádiové spektrum nebo fyzickou síťovou infrastrukturu (např. základnové stanice, uzly jádra sítě). VNO uzavírá komerční dohodu s hostitelským mobilním síťovým operátorem ([MNO](/mobilnisite/slovnik/mno/)), též nazývaným operátor mobilní síťové infrastruktury (MNIO), o hromadném nákupu přístupu k síťovým službám za velkoobchodní ceny. VNO tyto služby následně prodává pod vlastní značkou, často s vlastní cenotvorbou, marketingem a zákaznickou podporou.

Z technického a provozního hlediska se vztah mezi MNO a VNO může výrazně lišit hloubkou spolupráce, definovanou tzv. „modelem MVNO“. Na nejzákladnější úrovni (Branded Reseller nebo Light MVNO) VNO pouze přebranduje maloobchodní nabídku MNO. Pokročilejší modely zahrnují větší nezávislost: Thin MVNO provozuje vlastní systémy zákaznické péče, fakturace a marketingu, ale spoléhá na jádro sítě MNO. Thick MVNO navíc provozuje vlastní prvky jádra sítě, jako je [HLR](/mobilnisite/slovnik/hlr/)/[HSS](/mobilnisite/slovnik/hss/) (pro data účastníků) a [SMSC](/mobilnisite/slovnik/smsc/) (pro zasílání zpráv), a připojuje se k síti MNO prostřednictvím standardizovaných rozhraní. Full MVNO funguje téměř zcela nezávisle, spravuje vlastní jádro sítě a spoléhá na MNO pouze pro rádiový přístup a přenos.

Standardy 3GPP usnadňují model VNO definováním nezbytných rozhraní a procedur pro sdílení sítě a interakce mezi operátory. Klíčové specifikace pokrývají oblasti jako řízení roamingu (steering of roaming), kde VNO může ovlivnit, kterou partnerskou síť jeho účastníci použijí při roamingu, nebo architekturu Generic Bootstrapping Architecture ([GBA](/mobilnisite/slovnik/gba/)), která může být použita pro autentizaci. VNO spravuje vlastní identifikátory účastníků (rozsahy [IMSI](/mobilnisite/slovnik/imsi/)) a může implementovat vlastní servisní politiky, pravidla účtování a QoS profily. To vyžaduje integraci systémů VNO (jako [OSS](/mobilnisite/slovnik/oss/)/BSS) se sítí MNO, často prostřednictvím referenčních bodů, jako je rozhraní Np pro přenositelnost čísel nebo rozhraní S8 pro roaming v EPC.

Model VNO odděluje poskytování služeb od vlastnictví infrastruktury, čímž vytváří dynamičtější trh. Umožňuje MNO monetizovat nadbytečnou síťovou kapacitu, zatímco se VNO může zaměřit na niky trhu, inovativní balíčky služeb nebo specifické zákaznické segmenty bez masivních kapitálových výdajů potřebných pro vybudování fyzické sítě.

## K čemu slouží

Koncept VNO vznikl jako odpověď na tržní neefektivitu a vysoké bariéry vstupu v telekomunikačním průmyslu. Vybudování a provozování celostátní mobilní sítě vyžaduje obrovské kapitálové investice do spektrálních licencí a infrastruktury, což omezuje počet konkurentů. To může vést ke snížené konkurenci, vyšším cenám pro spotřebitele a pomalejší inovaci nabízených služeb. Model VNO byl vytvořen, aby zaváděl konkurenci na servisní vrstvě bez nutnosti budování nových fyzických sítí.

Řeší několik klíčových problémů. Hostitelským MNO poskytuje nový zdroj příjmů prostřednictvím monetizace nevyužívané síťové kapacity, zejména během mimopřepážkových hodin. Také jim umožňuje oslovit zákaznické segmenty, které jejich primární značka nemusí efektivně obsluhovat. Pro podnikatele a společnosti z jiných odvětví (např. retail, média) poskytuje proveditelnou cestu k vstupu na telekomunikační trh s využitím jejich stávajících zákaznických vztahů a síly značky. To vedlo k rozmachu specializovaných nabídek, jako jsou nízkonákladové tarify, tarify zaměřené na data pro tablety nebo tarify zabalené s obsahem od mediálních společností.

Z regulatorního hlediska mohou VNO pomoci dosáhnout politických cílů zvýšené konkurence a volby pro spotřebitele. Model se od svého zavedení ve 3GPP Release 8 významně vyvinul, přičemž standardy poskytují sofistikovanější technické nástroje pro hlubší síťovou integraci. Tento vývoj podporuje trend směrem k virtualizaci sítě a síťovým řezům v 5G, kde by v budoucnu mohl VNO provozovat vyhrazený end-to-end síťový řez pronajatý od MNO a nabízet vysoce přizpůsobené služby se zaručenými výkonnostními charakteristikami.

## Klíčové vlastnosti

- Poskytuje mobilní služby bez vlastnictví licencovaného spektra nebo infrastruktury rádiového přístupu
- Funguje pod vlastní komerční značkou a spravuje vlastní vztah se zákazníky
- Pronajímá síťovou kapacitu a služby od hostitelského mobilního síťového operátora (MNO)
- Může implementovat nezávislou zákaznickou péči, fakturaci, marketing a tarify
- V pokročilých modelech může provozovat vlastní prvky jádra sítě (HLR/HSS, SMSC)
- Využívá standardizovaná rozhraní 3GPP pro integraci se sítí hostitelského MNO

## Související pojmy

- [MNO – Mobile Network Operator](/mobilnisite/slovnik/mno/)
- [MVNO – Mobile Virtual Network Operator](/mobilnisite/slovnik/mvno/)
- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)
- [GWCN – GateWay Core Network](/mobilnisite/slovnik/gwcn/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 32.141** (Rel-19) — Subscription Management (SuM) Architecture
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security
- **TR 33.848** (Rel-18) — Technical Report on Virtualisation Security

---

📖 **Anglický originál a plná specifikace:** [VNO na 3GPP Explorer](https://3gpp-explorer.com/glossary/vno/)
