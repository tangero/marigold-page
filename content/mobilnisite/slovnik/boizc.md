---
slug: "boizc"
url: "/mobilnisite/slovnik/boizc/"
type: "slovnik"
title: "BOIZC – Barring of Outgoing InterZonal Calls"
date: 2025-01-01
abbr: "BOIZC"
fullName: "Barring of Outgoing InterZonal Calls"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/boizc/"
summary: "BOIZC je doplňková služba, která umožňuje operátorům sítí omezit účastníky v uskutečňování odchozích hovorů do destinací mimo jejich určenou geografickou zónu. Umožňuje řízení hovorů na základě zón pr"
---

BOIZC je doplňková služba, která umožňuje operátorům mobilních sítí zablokovat účastníkům možnost uskutečňovat odchozí hovory do destinací mimo jejich určenou geografickou zónu.

## Popis

BOIZC (Barring of Outgoing InterZonal Calls) je standardizovaná doplňková služba definovaná ve specifikacích 3GPP, která poskytuje operátorům sítí detailní kontrolu nad schopností účastníků uskutečňovat odchozí hovory mezi různými geografickými zónami. Služba funguje na úrovni core sítě, konkrétně v rámci architektury Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a Visitor Location Register (VLR), kde jsou udržovány a vynucovány profily služeb účastníků. Když se účastník pokusí uskutečnit hovor, síť ověří destinaci vůči předdefinovaným geografickým zónám a aplikuje logiku blokování na základě profilu předplatného služeb účastníka uloženého v HLR.

Technická implementace zahrnuje koordinaci několika síťových prvků. HLR ukládá předplatitelská data BOIZC jako součást profilu služeb účastníka, včetně konkrétních zón, ze kterých je účastníkovi zakázáno uskutečňovat odchozí hovory. Když účastník zahájí proceduru sestavení hovoru, Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) dotazuje VLR (který obsahuje kopii profilu služeb účastníka z HLR), aby zjistilo, zda cíl hovoru spadá do kategorie zakázaných mezizónových hovorů. MSC provádí geografickou analýzu volaného čísla vůči předdefinovaným definicím zón, které mohou být založeny na číslovacích plánech, kódech zemí nebo na specifických zónách definovaných operátorem sítě.

Definice zón jsou pro fungování BOIZC klíčové a jsou typicky konfigurovány v síťových databázích podle regionálních číslovacích plánů. Zóny mohou odpovídat zemím, konkrétním směrovým číslům nebo vlastním geografickým regionům definovaným operátorem pro účely účtování nebo regulatorních požadavků. Když pokus o hovor splní podmínku zakázané mezizónové komunikace, MSC odmítne sestavení hovoru s příslušným kódem příčiny, čímž zabrání jeho uskutečnění. Služba podporuje jak trvalé blokování (vždy aktivní), tak dočasné blokování (aktivované/deaktivované účastníkem nebo operátorem) režimy provozu.

BOIZC se integruje s dalšími doplňkovými službami a mechanismy řízení hovorů v síti. Funguje ve spojení se základními procedurami hovoru a interaguje se systémy účtování, aby zajistila správné účtování povolených hovorů. Služba také spolupracuje s dalšími blokovacími službami, jako je Barring of All Outgoing Calls ([BAOC](/mobilnisite/slovnik/baoc/)) a Barring of Outgoing International Calls ([BOIC](/mobilnisite/slovnik/boic/)), s konkrétními pravidly přednosti definovanými ve specifikacích 3GPP. Z pohledu signalizace využívá BOIZC protokoly [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) pro přenos profilu služeb mezi HLR a VLR a protokoly [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) nebo BICC (Bearer Independent Call Control) pro procedury sestavování a ukončování hovorů při rozhodování o blokování.

Služba hraje klíčovou roli v řízení síťových zdrojů a diferenciaci služeb. Řízením vzniku mezizónových hovorů mohou operátoři implementovat diferencované tarifní plány, předcházet úniku příjmů z neoprávněného mezinárodního volání a plnit regulatorní požadavky na omezení hovorů v konkrétních geografických oblastech. Implementace je pro účastníka během normálního provozu transparentní, ale poskytuje operátorům účinné nástroje pro správu a řízení služeb v komplexních síťových prostředích s více zónami.

## K čemu slouží

BOIZC byl vyvinut, aby řešil rostoucí potřebu geografického řízení hovorů v stále složitějších mobilních sítích, které pokrývají více zemí a regionů. Jak se mobilní sítě rozšiřovaly přes národní hranice prostřednictvím roamingových dohod a partnerství nadnárodních operátorů, vznikla potřeba detailnější kontroly vzniku hovorů na základě geografických zón. Tradiční blokovací služby jako [BAOC](/mobilnisite/slovnik/baoc/) (Barring of All Outgoing Calls) a BOIC (Barring of Outgoing International Calls) poskytovaly pouze binární nebo příliš širokou kontrolu, která neodpovídala jemněji odlišeným geografickým servisním oblastem, které operátoři potřebovali spravovat.

Před implementací BOIZC čelili operátoři výzvám při zavádění tarifních plánů založených na zónách a při plnění regulatorních požadavků, které se lišily podle geografického regionu. Například některé regulatorní rámce vyžadovaly omezení hovorů do konkrétních sousedních zemí nebo regionů, zatímco hovory do jiných povolovaly. Operátoři také potřebovali vytvářet servisní balíčky, které umožňovaly hovory v rámci určitých zón, zatímco hovory do jiných blokovaly, což umožňovalo sofistikovanější tarifní struktury a nabídky služeb. Omezení stávajících blokovacích služeb nutila operátory implementovat proprietární řešení, kterým chyběla interoperabilita a standardizace napříč různými dodavateli síťového vybavení.

Vytvoření BOIZC v 3GPP Release 4 poskytlo standardizovaný přístup k geografickému blokování hovorů, který mohl být konzistentně implementován v sítích více dodavatelů. Tato standardizace byla obzvláště důležitá, jak se sítě vyvíjely směrem ke složitějším architekturám s více servisními zónami a zvýšenými roamingovými scénáři. BOIZC umožnil operátorům implementovat přesné geografické kontroly, které odpovídaly jejich obchodním modelům, regulatorním závazkům a strategiím diferenciace služeb, při zachování interoperability a konzistentního uživatelského zážitku napříč různými síťovými implementacemi.

## Klíčové vlastnosti

- Blokování odchozích hovorů na základě geografických zón
- Integrace s profily služeb účastníka v HLR/VLR
- Podpora pro geografické zóny definované operátorem
- Kompatibilita se stávajícími procedurami sestavování a signalizace hovorů
- Spolupráce s dalšími doplňkovými blokovacími službami
- Standardizovaná implementace napříč sítěmi více dodavatelů

## Související pojmy

- [BAOC – Barring of All Outgoing Calls](/mobilnisite/slovnik/baoc/)
- [BOIC – Barring of Outgoing International Calls](/mobilnisite/slovnik/boic/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [BOIZC na 3GPP Explorer](https://3gpp-explorer.com/glossary/boizc/)
