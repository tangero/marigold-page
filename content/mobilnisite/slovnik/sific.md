---
slug: "sific"
url: "/mobilnisite/slovnik/sific/"
type: "slovnik"
title: "SIFIC – Send Information For Incoming Call"
date: 2025-01-01
abbr: "SIFIC"
fullName: "Send Information For Incoming Call"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sific/"
summary: "Doplňková služba v sítích GSM/UMTS, která umožňuje volanému účastníkovi před rozhodnutím o přijetí hovoru získat specifické informace o příchozím hovoru. Tyto informace, poskytnuté volající stranou, m"
---

SIFIC je doplňková služba v sítích GSM/UMTS, která od volající strany zasílá volanému účastníkovi informace o příchozím hovoru, jako je identita volajícího nebo důvod hovoru.

## Popis

Send Information For Incoming Call (SIFIC) je doplňková služba v okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) doméně, definovaná ve specifikacích 3GPP pro sítě GSM a UMTS. Funguje v rámci protokolu řízení hovoru (Call Control, [CC](/mobilnisite/slovnik/cc/)) na úrovni jádra sítě. Služba umožňuje volající straně připojit k žádosti o sestavení hovoru (zpráva SETUP) dodatečné informační prvky. Když je hovor směrován k volanému účastníkovi, síť tuto doplňkovou informaci doručí volanému uživatelskému zařízení (UE) současně s nebo před signálem upozornění na hovor (vyzváněním). Terminál volaného účastníka pak tyto informace může zobrazit na displeji, čímž poskytne kontext příchozího hovoru.

Technický tok zahrnuje několik síťových entit. SIFIC informace, pocházející z volajícího UE, je zahrnuta v informačním prvku FACILITY počáteční zprávy SETUP odeslané do ústředny [MSC](/mobilnisite/slovnik/msc/). MSC, která funguje jako výchozí ústředna, musí službu SIFIC rozpoznat a podporovat. Následně směruje hovor a připojená SIFIC data přes síť pomocí signalizace [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)), čímž zajišťuje transparentní přenos informací k cílové MSC obsluhující volaného účastníka. Cílová MSC zkontroluje profil služeb volaného účastníka, aby ověřila, zda je služba SIFIC zřízena a povolena. Pokud ano, přepošle SIFIC informaci volanému UE uvnitř zprávy SETUP přes rozhraní rádiového přístupu. Software uživatelského rozhraní (Man-Machine Interface, [MMI](/mobilnisite/slovnik/mmi/)) v UE je zodpovědný za parsování a zobrazení přijatého textu nebo identifikátoru uživateli.

Klíčové komponenty v architektuře zahrnují MSC, domácí lokační registr ([HLR](/mobilnisite/slovnik/hlr/)), který ukládá profil služeb účastníka indikující aktivaci SIFIC, a aplikační vrstvu řízení hovoru v UE. Služba je závislá na přesných signalizačních protokolech (např. [DTAP](/mobilnisite/slovnik/dtap/), ISUP) pro přenos informačního prvku FACILITY od konce ke konci. SIFIC se liší od služby prezentace čísla volajícího (CLIP); zatímco CLIP poskytuje pouze číslo volajícího (není-li omezeno), SIFIC umožňuje volajícímu aktivně odeslat zvolenou informaci. Tato služba vylepšuje základní telefonii přidáním vrstvy kontextu, což volané straně umožňuje stanovit prioritu hovorů, připravit se na konverzaci nebo se rozhodnout hovor přesměrovat na základě poskytnutého důvodu. Její implementace vyžaduje podporu jak od síťové infrastruktury, tak od koncových zařízení.

## K čemu slouží

SIFIC byl vyvinut, aby přidal inteligenci a kontext základním mobilním hlasovým hovorům a řešil tak omezení jednoduchého upozornění 'vyzváněním'. V raných mobilních sítích poskytoval příchozí hovor minimální informace – často jen indikaci příchozího hovoru, a pokud byla podporována a povolena služba CLIP, tak číslo volajícího. To ponechávalo volané straně málo kontextu pro rozhodnutí o důležitosti nebo naléhavosti hovoru. SIFIC byl vytvořen, aby toto vyřešil tím, že umožnil volajícímu proaktivně komunikovat účel hovoru, čímž se upozornění na hovor proměnilo v informativnější událost.

Historická motivace pochází z éry feature phone a rozšíření doplňkových služeb v GSM, s cílem napodobit nebo překonat funkce dostupné v pokročilých pevných sítích ISDN. Řešila obchodní a osobní komunikační potřeby, kdy vědět, *proč* někdo volá, může být stejně důležité jako vědět, *kdo* volá. Například volající mohl poslat "Naléhavé" nebo "Připomenutí schůzky", což umožnilo volané straně učinit okamžité, informované rozhodnutí o přijetí, odmítnutí nebo přesměrování hovoru na hlasovou schránku.

Tato služba také cílila na snížení zmeškaných hovorů a zbytečných zpětných volání tím, že poskytovala okamžitý kontext. Byla součástí sady doplňkových služeb GSM Phase 2+, navržených pro zvýšení hodnoty mobilních sítí nad rámec pouhé konektivity. Zatímco její použití záviselo na podpoře v zařízení a zřízení v síti, SIFIC představoval raný krok k bohatším komunikačním službám, které se později vyvinuly v multimediální zprávy a moderní služby rich communication services (RCS), čímž překlenul propast mezi jednoduchým hlasem a sdílením kontextu založeným na datech.

## Klíčové vlastnosti

- Umožňuje volající straně připojit k zprávě pro sestavení hovoru textový důvod nebo identifikátor
- Doručuje doplňkové informace zařízení volané strany před nebo spolu s upozorněním na hovor
- Funguje jako doplňková služba v okruhově spínané doméně s využitím informačních prvků FACILITY
- Vyžaduje zřízení v profilu účastníka v HLR a podporu v cílové MSC
- Zlepšuje rozhodování při zacházení s hovorem poskytnutím kontextu nad rámec čísla volajícího
- Je závislá na transparentnosti signalizace od konce ke konci napříč rozhraními ISUP a rádiovým rozhraním

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [SIFIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sific/)
