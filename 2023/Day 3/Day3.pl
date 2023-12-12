use warnings;
use Scalar::Util qw(looks_like_number);

package landmark;

sub is_integer {
   defined $_[0] && $_[0] =~ /^[+-]?\d+$/;
}

sub landmark_construct
{
    my $class_name = shift;
    my $self = {
        'startingX' => shift,
        'startingY' => shift,
        'endingX' => shift,
        'endingY' => shift,
        'value'=> shift,
        'used' => shift
    };
    bless $self, $class_name;
    return $self;
}

open(my $inFile, '<', "Day3.txt" ) or die "No File Found";
my @fileArr = <$inFile>;
my @numArry;
my @gearArray;
while (my ($Yidx, $line) = each @fileArr)
{
    my @splitString = split(//,$line);
    my $currentNum = '';
    my $startXidx = '';
    my $startYidx = '';
    while (my ($Xidx, $char) = each @splitString){
        
        unless($char eq '.')
        {
            if(is_integer($char))
            {
                
                if($currentNum eq '')
                {
                    $startXidx = $Xidx;
                    $startYidx = $Yidx;
                }
                $currentNum = $currentNum.$char;
                # print "$currentNum \n";
                
            }
            else
            {
                unless(ord($char)==10){
                    my $lmark =  landmark_construct landmark($Xidx,$Yidx,$Xidx, $Yidx,$char,'false');
                    push(@gearArray, $lmark);
                }
                
            }
            
        }
        else
        {
            unless($currentNum eq '')
            {
                $endX = $Xidx;
                $endY = $Yidx;
                if($startXidx eq $Xidx)
                {
                    $endY = $Yidx - 1;
                }
                elsif($startYidx eq $Yidx)
                {
                    $endX = $Xidx - 1;
                }
                my $lmark =  landmark_construct landmark($startXidx,$startYidx,$endX, $endY,$currentNum,'false');
                push(@numArry, $lmark);
                $currentNum = '';
                $startXidx = '';
                $startYidx = '';
            }
        }
    }
    
}
my $runningSum = 0;
foreach(@gearArray)
{
    # print "($_->{'value'}) ($_->{'startingX'},$_->{'startingY'}) is current gear\n";
    my $currentGear = $_;
    unless ($currentGear->{'value'} eq ' '){
        
        my $X = $currentGear->{'startingX'};
        my $Y = $currentGear->{'startingY'};
        # print "$_->{'value'} $_->{'startingX'} $_->{'startingY'} $_->{'endingX'} $_->{'endingY'}\n";
        
        foreach(@numArry)
        {
            # print "$_->{'value'} $_->{'startingX'} $_->{'startingY'} $_->{'endingX'} $_->{'endingY'}\n";
            my $Xtouching = 'false';
            my $Ytouching = 'false';
            if ( ($_->{'startingX'} >= ($X - 1)) and ($_->{'startingX'} <= ($X + 1)) ) {
                $Xtouching = 'true';
            }
            if ( ($_->{'endingX'} >= ($X - 1)) and ($_->{'endingX'} <= ($X + 1)) ) {
                $Xtouching = 'true';
            }
            if ( ($_->{'startingY'} >= ($Y - 1)) and ($_->{'startingY'} <= ($Y + 1)) ) {
                $Ytouching = 'true';
            }
            if ( ($_->{'endingY'} >= ($Y - 1)) and ($_->{'endingY'} <= ($Y + 1)) ) {
                $Ytouching = 'true';
            }
            if($Xtouching eq 'true' and $Ytouching eq 'true')
            {
                # print("$_->{'value'} ($_->{'startingX'},$_->{'startingY'})=>($_->{'endingX'},$_->{'endingY'})touching $currentGear->{'value'}\n");
                if($_->{'used'} eq 'false')
                {
                    $runningSum += $_->{'value'};
                    $_->{'used'} = 'true';
                    # print("\n$_->{'value'} used here\n\n");
                }
            }
           
        }
    }
}
print "$runningSum\n";

